from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

max_length = 0

class store(models.Model):
    storeId = models.IntegerField(max_length = 10, primary_key = True)
    storeName = models.CharField(max_length = 255)
    storeAddress = models.CharField(max_length = 255)

class webuser(models.Model):
    userID = models.IntegerField(max_length = 10, primary_key = True)
    userName = models.CharField(max_length = 255)
    phoneNumber = models.IntegerField(max_length = 11)
    emailAddress = models.EmailField()
    password = models.CharField(max_length = 255)
    deliveryAddress = models.CharField(max_length = 255)
    profession = models.CharField(max_length = 255)
    paymentID = models.IntegerField(max_length = 10)