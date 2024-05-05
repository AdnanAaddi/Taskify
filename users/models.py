from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ProjectUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='static/profile_pictures/', null=True, blank=True)
    class Meta:
        db_table="ProjectUser"
