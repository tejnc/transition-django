import os
from unicodedata import name 
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from social_auth import google, facebook
from .register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please try again."
            )
        
        #TODO: uncomment after frontend completion and test for specific application 
        # if user_data['aud'] != os.environ.get('GOOGLE_CLIENT_ID'):  # commented for testing purposes ; its needed to distinguish the app 
        #     raise AuthenticationFailed("oops, who are you?")

        print("user_data", user_data)
        user_id = user_data['sub']
        email = user_data["email"]
        name = user_data["name"]
        provider = "google"

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name
        )


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)

        try:
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            provider = 'facebook'
            return register_social_user(
                provider=provider,
                user_id=user_id,
                email=email,
                name=name,
            )
        except Exception as e:
            print(e)
            raise serializers.ValidationError(
                "The token is invalid or expired. Please try again."
            )