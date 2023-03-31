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
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

#forign key

class User_Register(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Test_Register(models.Model):
    tid = models.IntegerField(primary_key=True)
    tname = models.CharField(max_length=20)
    tdescription = models.CharField(max_length=100)
    price = models.IntegerField()

class Test_Book(models.Model):
    uid = models.ForeignKey(User_Register, on_delete=models.CASCADE)
    tname = models.ForeignKey(Test_Register, on_delete=models.CASCADE)
    dt = models.DateTimeField()

