import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# user - employee... address.....

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Address(BaseModel):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    tole = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=120)


    def __str__(self):
        return self.city


class EmergencyContact(BaseModel):
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=120)


    def __str__(self):
        return self.phone

class Employee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150,)
    attendance = models.IntegerField()
    id_card = models.IntegerField()
    driving_licence = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    salary = models.IntegerField()

    emp_address = models.ForeignKey(Address, related_name="emp_data", on_delete=models.CASCADE, null=True, blank=True)
    emp_emergency_contact = models.ForeignKey(EmergencyContact, related_name="emp_data1",on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    actions_performed = models.CharField(max_length=225)
    detail = models.TextField()


    def serialize_hook(self, hook):
        return {
            "hook": hook.dict(),
            "data": {
                "user": self.user.id,
                "email": self.email,
                "actions_performed":self.actions_performed,
                "detail":self.detail,
            }
        }

    def __str__(self):
        return self.actions_performed

class Hooks(models.Model):
    users_id = models.TextField()

    def __str__(self):
        return self.users_id