# import requests
# from rest_framework.response import Response

# from employee.models import Notifications


# WEBHOOK_URL = "http://0.0.0.0:8001/admin/webhooks/"

# data_format = {
#     "user": "tej",
#     "email" : "tej@email.com",
#     "actions_performed": "bought a shirt",
#     "detail": "quantity = 200"
# }

# def webhook_post(data:dict):
#     requests.post(WEBHOOK_URL, data=Response(data), headers={"Content-Type": "application/json"})
#     user = data["user"]
#     email = data["email"]
#     actions_performed = data["actions_performed"]
#     detail = data["detail"]

#     Notifications.objects.create(
#         user=user,
#         email=email,
#         actions_performed=actions_performed,
#         detail = detail,
#     )
#     return Response({"message": "notifications object created."})