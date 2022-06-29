from django.urls import path 

from .views import GoogleSocialAuthView

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view(), name='googlelogin'),
    path('facebook/', GoogleSocialAuthView.as_view(), name='googlelogin'),
]