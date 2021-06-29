from django.http import request
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from RestApi.models import Employee
from RestApi.serializers import Employeeseriallizer


@api_view(['GET','POST'])
def empapi(request):
    if request.method=='GET':
        id=request.data.get('id')
        print(f'Id is {id}')
        if id:
            emp=Employee.objects.get('id')
            serializer=Employeeseriallizer(emp)
        else:
            emp=Employee.objects.all()
            serializer=Employeeseriallizer(emp,many=True)
        return Response({'msg': "First restapi",'data':serializer.data })
    if request.method=='POST':
        serializer=Employeeseriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Call Post Data",'data':request.data})
        return Response({'msg':serializer.errors})



