from django.db import models



# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=10,default="")
    password = models.CharField(max_length=10,default="")
    phone = models.IntegerField(default=0)
    gender = models.CharField(max_length=6,default="")
    email = models.EmailField(max_length=10,default="")

    #def __str__(self):
        # return self.username
