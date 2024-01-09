from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_object(self, **kwargs):
        views = super().get_object()
        views.increase_views_count()
        return views


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'text', 'image', 'is_published')
    success_url = reverse_lazy('blog:post_list', )


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'slug', 'text', 'image', 'is_published')

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')