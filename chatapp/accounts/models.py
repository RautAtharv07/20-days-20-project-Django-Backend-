from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Userdata(AbstractUser):
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    
    
    