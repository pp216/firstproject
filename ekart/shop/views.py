from django.shortcuts import render

# Create your views here.
from .models import Signup
from .models import Signup


def signup_view(request):
    ee=Signup.objects.all()
    return render(request,'shop/index.html',{'ee':ee})

