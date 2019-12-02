from django.urls import path


from .views import (
    ArticleListView, articleListView,
    ArticleDetailView, articleDetailView,
    ArticleUpdateView, articleUpdateView,
    ArticleDeleteView, articleDeleteView,
    ArticleCreateView, articleCreateView,
)


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    #path('', articleListView, name='article_list'),
    #path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/', articleDetailView, name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    #path('<int:pk>/edit/', articleUpdateView, name='article_edit'),
    #path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/delete/', articleDeleteView, name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    #path('new/', articleCreateView, name='article_new'),
]