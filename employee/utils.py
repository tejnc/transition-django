from django.contrib.auth.models import User
from django_rest_webhooks.models import Hook
from rest_framework.response import Response

# from employee.serializers import HooksSerializer
# from .models import Hooks


def get_hook(username):
    user = User.objects.get(username__iexact=username)
    user_id = user.id

    

    # users_id = get_list()
    # print("type", type(user_id))
    # print("user_id", user_id)
    # print(users_id)
    # print(user_id in users_id)
    
    # if user_id in users_id:
    #     print("INSIDE IF")
    #     print(users_id)
    #     hook = Hook(
    #             user=user,
    #             event="notification.added",
    #             target="http://0.0.0.0:8001/webhook/",
    #         )
    #     print("hook", Hook)
    #     print("hook.user",hook)
    #     print("inside hook")
    #     return hook  # notification.added => http://0.0.0.0:8001/webhook/        
    # else:
    #     def get_list():
    #         print("Inside get list")
    #         hooks_obj = Hooks.objects.all()
    #         serializer = HooksSerializer(hooks_obj, many=True)
    #         if serializer.is_valid():
    #             users_id = serializer.validated_data.get("users_id")
    #             print("users_id", users_id)
    #             return list(users_id)

    #     print("INSIDE ELSE")
    #     hook = Hook(
    #             user=user,
    #             event="notification.added",
    #             target="http://0.0.0.0:8001/webhook/",
    #         )
    #     users_id = get_list()
    #     hook.save()
    #     users_id.append(user_id)
    #     print("users_id", users_id)
    #     Hooks.objects.create(
    #         users_id=users_id
    #     )
    #     print("hook event", hook.event) # notification event
    #     return hook

    # for testing purpose

    users_id = [7]

    if user_id in users_id:
        print("INSIDE IF")
        hook = Hook(
                user=user,
                event="notification.added",
                target="http://0.0.0.0:8001/webhook/",
            )
        print("hook", Hook)
        print("hook.user",hook)
        print("inside hook")
        return hook  # notification.added => http://0.0.0.0:8001/webhook/        
    else:
        print("INSIDE ELSE")
        hook = Hook(
                user=user,
                event="notification.added",
                target="http://0.0.0.0:8001/webhook/",
            )
        hook.save()
        print("users_id", users_id)
        print("hook event", hook.event) # notification event
        return hook
