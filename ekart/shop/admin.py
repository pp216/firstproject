from django.contrib import admin
from shop.models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ['username','password','email','phone','gender']
admin.site.register(Signup,SignupAdmin)


