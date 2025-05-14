from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserListCreateView, UserDetailView, UserSignupView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', UserSignupView.as_view(), name='signup'),  # 🔹 Signup route added
]
