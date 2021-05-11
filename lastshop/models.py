from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

##Tier 1 Independents
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

##Tier 2 Dependents
class driver(models.Model):
    userID = models.ForeignKey(webuser, related_name = 'driverUserID', on_delete = models.CASCADE)
    averageRating = models.DecimalField(max_digits = 65, decimal_places = 1, validators = [MaxValueValidator(5), MinValueValidator(1)])
    bank = models.CharField(max_length = 255)
    license = models.CharField(max_length = 255)
    mailAddress = models.CharField(max_length = 255)

class groceryorder(models.Model):
    orderID = models.IntegerField(max_length = 10, primary_key = True)
    deliveryAddress = models.ForeignKey(webuser, related_name = 'groceryDeliveryAddress', on_delete = models.CASCADE)
    deliveryDate = models.DateTimeField(default = timezone.now)
    userName = models.ForeignKey(webuser, related_name = 'groceryUserName', on_delete = models.CASCADE)
    phoneNumber = models.ForeignKey(webuser, related_name = 'groceryPhoneNumber', on_delete = models.CASCADE)
    instructions = models.TextField()
    paymentID = models.ForeignKey(webuser, related_name = 'groceryPaymentID', on_delete = models.CASCADE)
    subTotal = models.DecimalField(max_digits = 65, decimal_places = 2)
    deliveryFee = models.DecimalField(max_digits = 65, decimal_places = 2)
    tip = models.DecimalField(max_digits = 65, decimal_places = 2)
    total = models.DecimalField(max_digits = 65, decimal_places = 2)

class item(models.Model):
    itemID = models.IntegerField(max_length = 10, primary_key = True)
    itemName = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    image = models.URLField()
    brandName = models.CharField(max_length = 255)
    storeID = models.ForeignKey(store, on_delete = models.CASCADE)
    tagID = models.IntegerField(max_length = 10)

class paymentinfo(models.Model):
    paymentID = models.ForeignKey(webuser, on_delete = models.CASCADE) ##, primary_key = True
    cardName = models.CharField(max_length = 255)
    cardNumber = models.BigIntegerField(max_length = 16) ##, primary_key = True
    pinNumber = models.IntegerField(max_length = 4)
    expirationDate = models.DateField()
    billAddress = models.CharField(max_length = 255)
    default = models.BooleanField()

##Tier 3 Dependents
class cart(models.Model):
    userID = models.ForeignKey(webuser, on_delete = models.CASCADE) ##, primary_key = True
    itemID = models.ForeignKey(item, on_delete = models.CASCADE) ##, primary_key = True
    quantity = models.IntegerField()

class favorite(models.Model):
    userID = models.ForeignKey(webuser, on_delete = models.CASCADE) ##, primary_key = True
    itemID = models.ForeignKey(item, on_delete = models.CASCADE) ##, primary_key = True

class suborder(models.Model):
    orderId = models.ForeignKey(groceryorder, on_delete = models.CASCADE) ##, primary_key = True
    listID = models.IntegerField(max_length = 10) ##, primary_key = True
    subTotal = models.DecimalField(max_digits = 65, decimal_places = 2)
    tax = models.DecimalField(max_digits = 65, decimal_places = 2)
    total = models.DecimalField(max_digits = 65, decimal_places = 2)

class tag(models.Model):
    tagID = models.ForeignKey(item, on_delete = models.CASCADE) ##, primary_key = True
    tagName = models.CharField(max_length = 255) ##primary_key = True

##Tier 4 Dependents
class grocerylist(models.Model):
    listID = models.ForeignKey(suborder, on_delete = models.CASCADE) ##, primary_key = True
    itemID = models.ForeignKey(item, on_delete = models.CASCADE) ##, primary_key = True
    quantity = models.IntegerField()