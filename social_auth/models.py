from django.db import models

# Create your models here.
class SocialAuthUser(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    provider = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.email
