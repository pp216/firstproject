

#from RestApi.models import Employee
from rest_framework import serializers
from .models import Employee




class Employeeseriallizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['id','name','mobile','city']