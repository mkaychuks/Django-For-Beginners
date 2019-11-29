from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Post
from .forms import PostForm


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







class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['author', 'title', 'body']

# recreating BlogDetailView using Function-Based View...
def blogCreateView(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm()
    context = {'form': form}
    template_name = 'post_new.html'
    return render(request, template_name, context)





class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

# Recreating the UpdateView using Function Based View
def blogUpdateView(request, pk):
    form = PostForm()
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm()
    context = {'form': form}
    template_name = 'post_edit.html'
    return render(request, template_name, context)




class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# Recreating the DeleteView using Function Based View
def blogDeleteView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return reverse_lazy('home')