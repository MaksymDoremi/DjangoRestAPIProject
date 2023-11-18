from django.shortcuts import render, HttpResponse, redirect
from RestAPI.models import Author, Blog
import requests
from django.urls import reverse
from RestAPI.serializers import AuthorSerializer, BlogSerializer
from hashlib import sha256
from dotenv import load_dotenv
import os

load_dotenv()

# Create your views here.
def HelloWorld(request):
    return HttpResponse("Hello world")


def Login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']

        try:
            author = Author(Username=username, Password=sha256(f"{password}{os.getenv('SECRET_SALT')}".encode('utf-8')).hexdigest())
        
            # send POST reguest to api/login/
            url = request.build_absolute_uri(reverse('api_login'))
            data = requests.post(url, data=AuthorSerializer(author).data)
            print("AAAAAAAA")
            if data.status_code == 200:
                return redirect("homePage")
        except:
 
            error_message = "Bad credentials"
            return render(request, 'login.html', {'error_message': error_message})


def Registration(request):
    if request.method == "GET":
       return render(request, "registration.html")

    if request.method == "POST":
        # define POST variables
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        name = request.POST['nameInput']
        surname = request.POST['surNameInput']

        # create absolute uri to api/author/username/
        # api_author = request.build_absolute_uri(reverse('api_author_username'))

        # # use it to get author at api/author/username/input
        # data = requests.get(f"{api_author}{username}")
        # if data.status_code == 200:
        #     error_message = "Username already exists"
        #     return render(request, 'registration.html', {'error_message': error_message})

        # create author
        author = Author(Username=username, Password=sha256(f"{password}{os.getenv('SECRET_SALT')}".encode('utf-8')).hexdigest(), Name=name, Surname=surname)
        
        # send POST reguest to api/registration
        url = request.build_absolute_uri(reverse('api_registration'))
        data = requests.post(url, data=AuthorSerializer(author).data)

        # if created render registration with success message
        if data.status_code == 201:
            return render(request, "registration.html", {"success_message": "User registered successfully"})
        else:
            return render(request, "registration.html", {"error_message": "Bad reguest"})

def HomePage(request):
    if request.method == "GET":
        return HttpResponse("Login successful")

    