# # https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html

# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import Profile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
        
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    # NOTE: Copied from thinkster.io
    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `User` instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)