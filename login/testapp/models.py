from django.db import models

# Create your models here.
class Signup(models.Model):
    uname=models.CharField(max_length=28)
    pwd = models.CharField(max_length=28)
    mail = models.EmailField
    mob = models.IntegerField

class Login(models.Model):
    uname=models.CharField(max_length=28)
    pwd = models.CharField(max_length=28)