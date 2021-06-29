from django.urls import path
from . import views


urlpatterns = [


    path('signup',views.handleSignup,name='handlesignup'),
    path('home',views.home,name='home'),
    path('login',views.handlelogin,name='login'),
    path('nothome',views.nothome,name='nothome'),
    path('logout',views.handlelogout,name='logout'),
    path('out', views.out, name='out')
    ]

