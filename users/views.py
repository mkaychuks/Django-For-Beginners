from django.urls import reverse_lazy
from django.views.generic import CreateView


from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')