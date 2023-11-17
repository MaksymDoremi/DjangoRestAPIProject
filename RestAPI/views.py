from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Blog
from .serializers import AuthorSerializer, BlogSerializer, CreateBlogSerializer
from rest_framework.decorators import api_view

# def AllAuthors(request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return JsonResponse(serializer.data)
@api_view(["GET", "POST"])
def ApiAuthor(request, format=None):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})

    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "DELETE", "PATCH"])
def ApiBlogId(request, blog_id, format=None):
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
