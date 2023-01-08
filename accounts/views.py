from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView
from .renderers import UserJSONRenderer, ProfileJSONRenderer
from .exceptions import ProfileDoesNotExist

from .models import Profile

# Create your views here.
from .serializers import  (
    LoginSerializer, RegistrationSerializer, UserSerializer, ProfileSerializer,
)

class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer
    
    def post(self,request):
        user = request.data.get('user', {})
        
        # Checks if the is_valid tag is true using the validate method in the serializer
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """ View for accessing and updating user data """
    
    permission_classes  = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """ Returns serializer data """
        
        serializer = self.serializer_class(request.user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        """ Allows user fields to be updated, including password """
        user_data = request.data.get('user', {})
                       
        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'email': user_data.get('email', request.user.email),
            
            'profile': {
                'first_name': user_data.get('first_name', request.user.profile.first_name),
                'last_name': user_data.get('last_name', request.user.profile.last_name),
                'bio': user_data.get('bio', request.user.profile.bio),
                'image': user_data.get('image', request.user.profile.image),
                'date_of_birth': user_data.get('date_of_birth', request.user.profile.date_of_birth),                
            }    
        }
        
        # Serialize, validate, save pattern
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer

    ### NOTE: DOCUMENTATION COPIED FROM THINKSTER.io
    def retrieve(self, request, username, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related('user').get(
                user__username=username
            )
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)