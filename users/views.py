from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework import generics

from .serializers import UserSerializer, UserCreateSerializer

# Use the custom or default user model
User = get_user_model()


class UserSignupView(CreateView):
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    fields = ['username', 'email', 'password']

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)  # This properly hashes the password
        user.save()
        return super().form_valid(form)


# 🔹 API Views (DRF)
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
