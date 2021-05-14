from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

max_length = 0

class webuser(models.Model):
    userID = models.IntegerField(max_length = 10, primary_key = True)
    userName = models.CharField(max_length = 255)
    phoneNumber = models.IntegerField(max_length = 11)
    emailAddress = models.EmailField()
    password = models.CharField(max_length = 255) #widget=forms.PasswordInput)
    deliveryAddress = models.CharField(max_length = 255)
    profession = models.CharField(max_length = 255)
    paymentID = models.IntegerField(max_length = 10)

class Profile(models.Model):
    userName = models.CharField(max_length = 255)
    phoneNumber = models.IntegerField(max_length = 11)
    emailAddress = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    deliveryAddress = models.CharField(max_length = 255)
    profession = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.userName, self.password}'


