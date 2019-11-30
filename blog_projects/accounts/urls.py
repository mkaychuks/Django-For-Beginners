from django.urls import path


from .views import SignUpView, signUpView

urlpatterns = [
   # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', signUpView ,name='signup')
]