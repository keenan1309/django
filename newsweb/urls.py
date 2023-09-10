from django.contrib import admin
from django.urls import path
from newsweb import views
from django.views.generic import ListView, DetailView
from .models import Post


urlpatterns = [
    path('index/<int:pk>',
    ListView.as_view(
    queryset=
    Post.objects.all().order_by("-date")[:25],
    template_name="postid.html"
)
),
path('index/<int:pk>/',
    DetailView.as_view(
    model = Post,
    template_name="article.html"
)
),
]