from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
# from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from django_rest_webhooks.models import Hook

from .serializers import EmployeeSerializer, EmployeeListSerializer, NotificationCreateSerializer
from .models import EmergencyContact, Employee, Address, Notification
from .utils import get_hook
# from utils import webhooks
# Create your views here.


# class ProfileViewset(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     http_method_names = ['get','post','retrieve','put','patch']


class EmployeeRegistrationAPIView(APIView):
    # @swagger_auto_schema(request_body= EmployeeSerializer, tags=["Testing"], operation_summary="Creating Employee" )
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer

    @extend_schema(tags=["Employee"])
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            full_name = serializer.validated_data.get("full_name")
            attendance = serializer.validated_data.get("attendance")
            id_card = serializer.validated_data.get("id_card")
            driving_licence = serializer.validated_data.get("driving_licence")
            blood_group = serializer.validated_data.get("blood_group")
            salary = serializer.validated_data.get("salary")
            tole = serializer.validated_data.get("tole")
            city = serializer.validated_data.get("city")
            zip_code = serializer.validated_data.get("zip_code")
            country = serializer.validated_data.get("country")
            emergency_phone = serializer.validated_data.get("emergency_phone")
            emergency_email = serializer.validated_data.get("emergency_email")

            user = User.objects.create_user(
                username = username, email=email, password=password
            )

            emp_address = Address.objects.create(
                tole=tole, city=city, zip_code=zip_code, country=country
            )
            emp_address.save()

            emp_emergency_contact = EmergencyContact.objects.create(
                phone=emergency_phone, email=emergency_email
            )
            emp_emergency_contact.save()
            print("emp_emergency_contact.id", emp_emergency_contact.id )
            
            employee = Employee.objects.create(
                user=user, full_name=full_name, attendance=attendance,id_card=id_card,
                driving_licence=driving_licence, blood_group=blood_group, salary=salary,
                emp_address=emp_address, emp_emergency_contact=emp_emergency_contact
            )
            employee.save()

            user_notify = User.objects.get(username__iexact="testing_employee")
            notification_obj = Notification.objects.create(
                user=user_notify,
                email=email,
                actions_performed="testing",
                detail="testing",
            )
            notification_obj.save()

            resp = {
                "status": status.HTTP_201_CREATED,
                "message": "Employee successfully created."
            }
            return Response(resp)
        else:
            resp = {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": serializer.errors
            }
            return resp


class EmployeeListAPIView(APIView):
    serializer_class = EmployeeListSerializer
    # @swagger_auto_schema(tags=["Testing"], operation_summary="List Employee" )
    # permission_classes = [permissions.IsAuthenticated]
    @extend_schema(summary="listing employees", tags=["Employee"])
    def get(self, request):
        emp = Employee.objects.all()
        print("emp", emp)
        serializer = EmployeeListSerializer(emp, many=True)
        return Response(serializer.data)


class NotificationCreateAPIView(APIView):
    serializer_class = NotificationCreateSerializer

    @extend_schema(tags=["Notification"])
    def post(self, request):
        user = User.objects.get(username__iexact="testing_employee")
        get_hook(username="testing_employee")

        serializer = NotificationCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            actions_perfomed = serializer.validated_data.get("actions_performed")
            detail = serializer.validated_data.get("detail")
            notification_obj = Notification.objects.create(
                user=user,
                email=email,
                actions_performed=actions_perfomed,
                detail=detail,
            )
            notification_obj.save()
            return Response({"message": "notification saved"})


        

class WebhookReceivedAPIView(APIView):

    @extend_schema(tags=["Test"])
    def post(self, request):
        print("Data received from Webhook is", request.data["data"])
        return HttpResponse("Webhook received")

