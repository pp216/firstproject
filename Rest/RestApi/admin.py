from django.contrib import admin

# Register your models here.
from RestApi.models import Employee


@admin.register(Employee)
class Employeeadmin(admin.ModelAdmin):
    list_display = ['id','name','mobile','city']