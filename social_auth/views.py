from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from drf_spectacular.utils import extend_schema

from .serializers import FacebookSocialAuthSerializer, GoogleSocialAuthSerializer


class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    @extend_schema(tags=["Social Auth"])
    def post(self, request):
        """
        POST with "auth_token"

        Send an idtoken received from google to Google to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class FacebookSocialAuthView(GenericAPIView):
    serializer_class = FacebookSocialAuthSerializer

    def post(self, request):
        """
        POST with "auth_token" 

        Send an auth token to get user information
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)