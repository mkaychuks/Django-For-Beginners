from django.urls import path


from .views import (
    BlogListView, blogListView,
    BlogDetailView, blogDetailView
)


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    # path('', blogListView, name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/', blogDetailView, name='post_detail'),
]