
from django.db import models

# Create your models here.

class StudentReg(models.Model):
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=10)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=50)

# class NameFormModel(models.Model):
#     name=models.CharField(max_length=100)
#     password=models.CharField(max_length=20)
    

