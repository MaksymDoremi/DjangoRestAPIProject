from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from RestAPI.models import Author, Blog
import requests
from rest_framework.response import Response
from django.urls import reverse
from RestAPI.serializers import AuthorSerializer, BlogSerializer, CreateBlogSerializer
from hashlib import sha256
from dotenv import load_dotenv
import os
import datetime

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

		author = Author(Username=username, Password=sha256(
			f"{password}{os.getenv('SECRET_SALT')}".encode('utf-8')).hexdigest())

		# send POST reguest to api/login/
		url = request.build_absolute_uri(reverse('api_login'))
		response = requests.post(url, data=AuthorSerializer(author).data)

		if response.status_code == 200:
			print(response.json().get("user", {}).get("Username"))
			request.session['id'] = response.json().get('user', {}).get('id')
			request.session['Username'] = response.json().get(
				'user', {}).get("Username")
			request.session['Name'] = response.json().get(
				'user', {}).get("Name")
			request.session['Surname'] = response.json().get(
				'user', {}).get("Surname")
			return redirect("homePage")
		else:

			error_message = response.json().get("error")
			print(error_message)
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
		author = Author(Username=username, Password=sha256(
			f"{password}{os.getenv('SECRET_SALT')}".encode('utf-8')).hexdigest(), Name=name, Surname=surname)

		# send POST reguest to api/registration
		url = request.build_absolute_uri(reverse('api_registration'))
		response = requests.post(url, data=AuthorSerializer(author).data)

		# if created render registration with success message
		if response.status_code == 201:
			return render(request, "registration.html", {"success_message": "User registered successfully"})
		else:
			return render(request, "registration.html", {"error_message": response.json().get("error")})


def HomePage(request):
	if request.method == "GET":
		if "Username" in request.session.keys():

			url = request.build_absolute_uri(
				reverse("api_author_username", args=[request.session['Username']]))

			response = requests.get(url)
			return render(request, "homePage.html", {"user": response.json()})
		else:
			return redirect("login")


def PostBlog(request):
	if request.method == "POST":
		# define POST variables
		author = Author.objects.get(id=request.session['id'])
		content = request.POST['blog_content']
		date = datetime.date.today()

		data = {'Author': author.id, 'Content': content, 'Date': date}
		
		url = request.build_absolute_uri(reverse("api_blog"))

		response = requests.post(url, data=data)

		serializer = AuthorSerializer(author)

		if response.status_code == 201:
			return render(request, "homePage.html", {"success_message": "Blog created", "user": serializer.data})
		else:
			#return render(request, "homePage.html", {"error_message": response.json().get("error")})
			return HttpResponse(response)


def Logout(request):
	if request.method == "POST":
		del request.session['Username']
		request.session.modified = True
		return render(request, 'logout.html')
	
def Blogs(request):
	if request.method == "GET":
		if "Username" in request.session.keys():
			url = request.build_absolute_uri(reverse("api_blog"))
			response = requests.get(url)
			return render(request, "blogs.html", {"blogs": response.json().get("blogs")})
