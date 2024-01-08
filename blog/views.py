from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('blog:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'text', 'image', )
    success_url = reverse_lazy('blog:list')




