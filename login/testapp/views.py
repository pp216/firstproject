from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render,  redirect



# Create your views here.
from .models import Signup, Login


#from .models import Login


def home(request):
    return HttpResponse("<H1>welcome to home page</H1>")










def signup(request):
    if request.method == "POST":
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        eml = request.POST.get("email")
        mob = request.POST.get("mobile")
        username=request.POST.get("username")
        password=request.POST.get("password")
        print("My firstname is {}".format(fname))
        print("My lastname is {}".format(lname))
        print("My email is {}".format(eml))
        print("My Number is {}".format(mob))
        print("My username is {}".format(username))
        print("My password is {}".format(password))
        obj = Signup(50,fname,lname,eml,mob,username,password)
        obj.save()
        result = Signup.objects.all()
        print(result)






    return  render(request,'testapp/signup.html')





def login(request):
    if request.method == "POST":
            username1 = request.POST.get("username")
            password1= request.POST.get("password")

            print("My username is {}".format(username1))
            print("My password is {}".format(password1))

            x=auth.authenticate(username=username1,password=password1)
            if x is None:
             return HttpResponse("<H1>Invalid username or password</H1>")
            else:
              return  redirect('home')

            obj = Login(50,username1,password1)
            obj.usname=username1
            obj.pswd=password1
            obj.save()
            result = Signup.objects.all()
            print(result)
    else:
      return HttpResponse("Not Found")


def about(request):
    return HttpResponse("<H1>About Page</H1>")
