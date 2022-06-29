import os
import random
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from dotenv import load_dotenv

from .models import SocialAuthUser
from employee.tokens import get_tokens_for_user

load_dotenv()

def generate_username(name):
    """
    Generates username 
    """
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = SocialAuthUser.objects.filter(email=email)

    if filtered_user_by_email.exists():    
        if provider == filtered_user_by_email[0].provider:
            user_obj = User.objects.filter(email=email).first()
            print("user object", user_obj)
            print("type of user object", type(user_obj))
            registered_user = authenticate(
                username=user_obj,
                password=os.environ.get('TESTPASSWORD'),
            )
            print("username", registered_user.username)
            print("password", registered_user.password)
            return {
                "username": registered_user.username,
                "email": registered_user.email,
                "tokens": get_tokens_for_user(user_obj),
            }
        else: 
            raise AuthenticationFailed(
                detail="Please continue you login using" + filtered_user_by_email[0].auth_provider
            )
    
    else:
        username = generate_username(name)
        social_auth_user = SocialAuthUser.objects.create(
            name=name,
            username=username,
            email=email,
            provider=provider,
        )
        social_auth_user.save()
        user_obj = User.objects.create_user(
            username=username,
            email=email,
            password=os.environ.get('TESTPASSWORD'),
        )
        
        new_user = authenticate(
            username=username,
            password=os.environ.get('TESTPASSWORD'),
        )
        print("password from env", os.environ.get('TESTPASSWORD'))
        print("new_user", new_user)
        print("newUser password", new_user.password)
        return {
                "username": new_user.username,
                "email": new_user.email,
                "tokens": get_tokens_for_user(user_obj),
            }