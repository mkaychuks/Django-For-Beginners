from django.views.generic import (
    ListView, DetailView, UpdateView,
    DeleteView, CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy


from .models import Article
from .forms import ArticleForm, ArticleCreateForm


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    login_url = 'login'

def articleListView(request):
    articles = Article.objects.all()
    context = {'articles': articles }
    template_name = 'article_list.html'
    return render(request, template_name, context)




class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

def articleDetailView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    template_name = 'article_detail.html'
    context = {
        'article': article
    }
    return render(request, template_name, context)





class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

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

            
















class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

def articleDeleteView(request,pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')









class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
    