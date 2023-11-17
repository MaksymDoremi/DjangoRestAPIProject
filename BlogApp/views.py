from django.shortcuts import render, HttpResponse, redirect
from RestAPI.models import Author, Blog
import requests
from django.urls import reverse
from RestAPI.serializers import AuthorSerializer, BlogSerializer

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
            teacher = Author.objects.get(Username=username, Password=password)
            # request.session['username'] = teacher.Username
            # request.session['currentRole'] = "t"
            return redirect("homePage")
        except:
 
            error_message = "Bad credentials"
            return render(request, 'login.html', {'error_message': error_message})


def Registration(request):
    if request.method == "GET":
       return render(request, "registration.html")

    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        name = request.POST['nameInput']
        surname = request.POST['surNameInput']

        url = request.build_absolute_uri(reverse('api_author'))

        data = requests.get(f"{url}username/{username}")
        if data.status_code == 200:
            error_message = "Username already exists"
            return render(request, 'registration.html', {'error_message': error_message})

        author = Author(Username=username, Password=password, Name=name, Surname=surname)
        
        requests.post(url, data=AuthorSerializer(author).data)

        return render(request, "registration.html", {"success_message": "User registered successfully"})


def HomePage(request):
    if request.method == "GET":
        pass

    