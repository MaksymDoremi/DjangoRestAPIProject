"""
URL configuration for RestAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/login/", views.Login, name="api_login"),
    path("api/registration/", views.Registration, name="api_registration"),
    path("api/blog/", views.ApiBlog, name="api_blog"),
    path("api/blog/blogId/<int:blog_id>", views.ApiBlogId, name="api_blog_id"),
    path("api/author/", views.ApiAuthor),
    path("api/author/username/<str:username>", views.ApiAuthorUsername,  name="api_author_username"),
    path("", include("BlogApp.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
