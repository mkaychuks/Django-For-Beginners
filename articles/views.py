from django.views.generic import (
    ListView, DetailView, UpdateView,
    DeleteView, CreateView
)
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy


from .models import Article
from .forms import ArticleForm, ArticleCreateForm


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

def articleListView(request):
    articles = Article.objects.all()
    context = {'articles': articles }
    template_name = 'article_list.html'
    return render(request, template_name, context)




class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

def articleDetailView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    template_name = 'article_detail.html'
    context = {
        'article': article
    }
    return render(request, template_name, context)





class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

def articleUpdateView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    template_name = 'article_edit.html'
    return render(request, template_name, context)

            
















class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

def articleDeleteView(request,pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')









class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)

def articleCreateView(request):
    form = ArticleCreateForm()
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleCreateForm()
    context = {
        'form':form
    }
    template_name = 'article_new.html'
    return render(request, template_name, context)
    