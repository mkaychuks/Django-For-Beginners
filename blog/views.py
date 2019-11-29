from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class BlogListView(ListView):
    template_name = 'home.html'
    context_object_name = 'posts'
    model = Post

# Recreating the ListView using Function Based View   
def blogListView(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    template_name = 'home.html'
    return render(request, template_name, context)



class BlogDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

# recreating BlogDetailView using Function-Based View...
def blogDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    template_name = 'post_detail.html'
    context = {
        'post': post
    }
    return render(request, template_name, context)
