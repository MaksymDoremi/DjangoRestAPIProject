from django.http import JsonResponse
from .models import Author, Blog
from .serializers import AuthorSerializer, BlogSerializer

def AllAuthors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True) 
    return JsonResponse(serializer.data)


def AllBlogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True) 
    return JsonResponse({"blogs":serializer.data}, safe=False)


def BlogId(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    serializer = BlogSerializer(blog, many=True)
    return JsonResponse({"blogs":serializer.data}, safe=False)