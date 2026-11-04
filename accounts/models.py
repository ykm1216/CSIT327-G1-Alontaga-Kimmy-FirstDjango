from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        INSTRUCTOR = 'INSTRUCTOR', 'Instructor'
        ADMIN = 'ADMIN', 'Admininstrator'
        

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    course = models.CharField(max_length=100, blank=True, null=True)