from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloWorld),
    path("login/", views.Login, name='login'),
    path("registration/", views.Registration, name="registration"),
    path("homePage", views.HomePage, name="homePage")
]
