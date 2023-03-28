from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    #gender = models.CharField(max_length=15)
    TYPE_SELECT = (
        ('female', 'Female'),
        ('male', 'Male'),
    )
    gender = models.CharField(max_length=11, choices=TYPE_SELECT, default=None)
    contact = models.IntegerField()
    password = models.CharField(max_length=20)

class employee2(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=15)
    contact = models.IntegerField()
    password = models.CharField(max_length=20)

class fileUpload(models.Model):
    name = models.CharField(max_length=20)
    file = models.FileField()

#food
class uploadModel(models.Model):
    iname = models.CharField(max_length=20)
    iprice = models.IntegerField()
    file = models.FileField()
class itemBillModel(models.Model):
    iname = models.CharField(max_length=20)
    iprice = models.IntegerField()
    qty = models.IntegerField()
    total = models.IntegerField(null=True)

#login


