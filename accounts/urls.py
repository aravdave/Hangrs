from django.urls import re_path

from .views import (
    RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, ProfileRetrieveAPIView
)

app_name = 'accounts'
urlpatterns = [
    re_path(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    re_path(r'^users/?$', RegistrationAPIView.as_view()),
    re_path(r'^users/login/?$', LoginAPIView.as_view()),
    re_path(r'^profiles/<str:username>', ProfileRetrieveAPIView.as_view()),
]