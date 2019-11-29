from django.urls import path


from .views import (
    BlogListView, blogListView,
    BlogDetailView, blogDetailView,
    BlogCreateView, blogCreateView,
    BlogUpdateView, blogUpdateView,
    BlogDeleteView, blogDeleteView
)

# from imports in .views, I placed each CBV with
# its corresponding FBV so as to make things clear..


# ALl the hashed(#) parts are links to the FBV option of
# its respective view

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    # path('', blogListView, name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/', blogDetailView, name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    #path('post/new/', blogCreateView, name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    #path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/delete/', blogDeleteView, name='post_delete'),
]