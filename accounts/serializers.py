# https://thinkster.io/tutorials/django-json-api/authentication

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Profile

class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializer for registering a new user"""
    
    # It's necessary to specify the password field to enforce that a password is given
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The read_only property requires that a token is NOT passed in (because why would they be logging in then?)
    token = serializers.CharField(max_length=255, read_only=True)

    # Specifies the model being serialized and all the fields that will passed to the serializer at some point
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    # specifies that the create function in CRUD creates a new user using the custom User model and create_user function
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    """ Serializer for logging in a returning user (doesn't inherit ModelSerializer"""
    
    # Specifies all of the relevant serializer fields, some with certain permissions that are appropriate for logging in
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    # Only has validate function (not CRUD)
    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)


        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # Django's authenticate method handles verifying a email/password combo exists
        # Note that since we used email as USERNAME_FIELD in the model, email is used 
        # for the username parameter
        user = authenticate(username=email, password=password)

        # If no such user exists, user will be assigned to None
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        # Uses Django's is_active flag to check if the account was deactivated
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # Returns a dictionary of validated data that's used for CRUD operations    
        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'bio',
            'image',
            'date_of_birth',
            'confirmed'
        )
        read_only_fields = ('username', 'confirmed')

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://freesvg.org/img/abstract-user-flat-1.png'

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User info."""

    # Enforces that passwords are write_only and follow the default min and max length
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    
    profile = ProfileSerializer(write_only=True)
    first_name = serializers.CharField(source='profile.first_name', read_only=True)
    last_name = serializers.CharField(source='profile.last_name', read_only=True)
    bio = serializers.CharField(source='profile.bio', read_only=True)
    image = serializers.URLField(source='profile.image', read_only=True)
    date_of_birth = serializers.DateField(source='profile.date_of_birth', read_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token', 'profile', 'first_name',
                  'last_name', 'bio', 'image', 'date_of_birth')
        read_only_fields = ('token',)

    # U in CRUD
    def update(self, instance, validated_data):
        """Updates user info"""

        # Saves the password for DRF's 
        password = validated_data.pop('password', None)
        
        profile_data = validated_data.pop('profile', {})

        # sets the new value to the corresponding attribute of instance
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        # Uses DRF's robust password protocal
        if password is not None:
            instance.set_password(password)

        # Must save the instance after every modification
        instance.save()
        
        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)
            
        instance.profile.save()

        return instance