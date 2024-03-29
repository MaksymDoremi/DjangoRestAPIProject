from rest_framework import serializers
from .models import Author, Blog


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'Username', 'Password', 'Name', 'Surname']


class BlogSerializer(serializers.ModelSerializer):
    Author = AuthorSerializer()

    class Meta:
        model = Blog
        fields = ['id', 'Content', 'Date', 'Author']


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:

        model = Blog
        fields = ['id', 'Content', 'Date', 'Author']
