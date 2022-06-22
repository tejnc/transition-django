from rest_framework import serializers
from employee.models import Address, Employee, EmergencyContact, Hooks, Notification
# from utils.validation import CustomPasswordValidation


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = "__all__"


class EmergencyContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmergencyContact
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_null=False)
    email = serializers.EmailField()
    password = serializers.CharField(allow_null=False)
    confirm_password = serializers.CharField(allow_null=False)
    tole = serializers.CharField()
    city = serializers.CharField()
    zip_code = serializers.IntegerField()
    country = serializers.CharField()
    emergency_phone = serializers.CharField()
    emergency_email = serializers.CharField()
    

    class Meta:
        model = Employee
        fields = ("username","email", "password","confirm_password","full_name", "attendance", "id_card", "driving_licence",
        "blood_group", "salary", "tole", "city", "zip_code", "country", "emergency_phone","emergency_email"
        )

    # def validate(self, attrs):
    #     return CustomPasswordValidation.validate_password(attrs=attrs,
    #         password=attrs.get("password"),
    #         confirm_password=attrs.get("confirm_password")
    #     )
    

    def validate(self, attrs):
        SPECIAL_SYMBOL = ['$', '@', '#', '%', '!', '^', '&', '*']
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        print("password", password)
        print("confirm_password", confirm_password)

        if password != confirm_password:
            raise serializers.ValidationError(
                "Passwords did not match!"
            )
        if len(password)<8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )
        if len(password) > 12:
            raise serializers.ValidationError(
                "The new password should not be greater than 12 characters long."
            )
        first_isalpha = password[0].isalpha()
        if all(c.isalpha()==first_isalpha for c in password):
            raise serializers.ValidationError(
                "New password must be at least one letter and  at least one digit or punctuation character."
            )
        first_isupper = password[0].isupper()
        if all(c.isupper() == first_isupper for c in password):
            raise serializers.ValidationError(
                "The new password must contain at least one Uppercase Letter."
            )
        if not any(c in SPECIAL_SYMBOL for c in password):
            raise serializers.ValidationError(
                "The password must contain at least one Special Symbols."
            )
        return attrs


class EmployeeListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    full_name = serializers.CharField()
    attendance = serializers.IntegerField()
    id_card = serializers.IntegerField()
    driving_licence = serializers.IntegerField()
    blood_group = serializers.CharField()
    salary = serializers.IntegerField()


    emp_address = serializers.SerializerMethodField()
    emp_emergency_contact = serializers.SerializerMethodField()


    class Meta:
        model = Employee 
        fields = [ 
            "username",
            "full_name",
            "attendance",
            "id_card",
            "driving_licence",
            "blood_group",
            "salary",
            "emp_address",
            "emp_emergency_contact",
        ]

    def get_username(self, obj) -> str:
        if obj.user.username:
            return obj.user.username
        else:
            return "No username"


    def get_emp_address(self, obj) -> dict:
        print("address obj",obj)
        emp_address = Address.objects.get(id=obj.emp_address.id)
        return AddressSerializer(emp_address).data  #  context={"request":self.context["request"]}

    def get_emp_emergency_contact(self, obj) -> dict:
        print("emergency obj",obj)
        print("emergency id", obj.emp_emergency_contact.id)
        emp_emergency = EmergencyContact.objects.get(id=obj.emp_emergency_contact.id)
        return EmergencyContactSerializer(emp_emergency).data  #  context={"request":self.context["request"]}


class NotificationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Notification
        fields = [
            "email",
            "actions_performed",
            "detail",
        ]


class HooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hooks
        fields = [ 
            "users_id"
        ]