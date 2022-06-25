from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
class PostListView(ListView):
    model=Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")



