from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('technician','Technician'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone = models.BigIntegerField(blank=True, null=True, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    national_id = models.CharField(max_length=20, blank=True, null=True)
    certificate = models.BinaryField(blank=True, null=True)
    profile_picture = models.BinaryField(blank=True, null=True)


    def is_confirmed(self):
        return self.confirmed

    def set_confirmed(self):
        self.confirmed = True
        self.save()

    def __str__(self):
        return self.username
    class Meta():
        db_table ="users"