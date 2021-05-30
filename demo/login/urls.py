from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),

    path('signup',views.handleSignup,name='handleSignup'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('login', views.handlelogin, name='login'),
    path('home',views.home,name='home'),
    path('nothome',views.nothome,name='nothome'),
    path('out', views.out, name='out'),
    path('users', views.users, name='users'),
    path('profile', views.profile, name='profile')


]