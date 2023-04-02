from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.CharField(max_length=30)
    phone = models.IntegerField(null=True)

    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class TeacherRegistration(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)

    Qualification = models.CharField(max_length=50)
    Introduction_brief = models.CharField(max_length=100)
