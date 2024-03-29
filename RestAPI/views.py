from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Author, Blog
from .serializers import AuthorSerializer, BlogSerializer, CreateBlogSerializer


# def AllAuthors(request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return JsonResponse(serializer.data)
@api_view(["GET"])
def ApiAuthor(request, format=None):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})

    return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET"])
def ApiAuthorUsername(request, username, format=None):
    if request.method == "GET":
        authors = Author.objects.get(Username=username)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def ApiBlog(request, format=None):

    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response({"blogs": serializer.data})

    if request.method == "POST":
        serializer = CreateBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "bad request during creating blog"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "DELETE", "PATCH"])
def ApiBlogId(request, blog_id, format=None):
    # if 'Username' in request.session.keys():
    try:
        blog = Blog.objects.get(id=blog_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":

        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = CreateBlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # else:
    #     return HttpResponse("Not authenticated")


@api_view(["POST"])
def Login(request):
    if request.method == "POST":
        user = None
        try:
            user = Author.objects.get(
                Username=request.data['Username'], Password=request.data['Password'])
        except:
            pass

        if user is None:
            print(f"{request.data['Password']}")
            return Response({"error": "Incorrect username or password"}, status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = AuthorSerializer(user)
            return Response({"user": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def Registration(request):
    if request.method == "POST":
        # get data from registration form into serializer
        serializer = AuthorSerializer(data=request.data)
        # get user with that username
        user = Author.objects.filter(Username=request.data['Username'])
        # if that username exists than return and error
        if user:
            return Response({"error": "User already exists bruh"}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            user = Author.objects.get(Username=request.data['Username'])
            user.save()
            return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
