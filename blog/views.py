from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class BlogListView(ListView):
    template_name = 'home.html'
    context_object_name = 'posts'
    #model = Post
    
    def get_queryset(self):
        post = Post.objects.order_by('-title')
        return post