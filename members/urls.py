from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('book/', views.book, name='book'),
    path("register/", views.register, name="register"),
    path('login/', views.login, name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('logout/', views.logout, name='logout'),

] 