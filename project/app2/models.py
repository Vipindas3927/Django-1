from django.db import models

# Create your models here.
class user_data_model(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.IntegerField()
