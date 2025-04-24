# from django.urls import path
# from .views import UserListView, UserDetailView, UserCreateView
# urlpatterns = [
#     path('list',UserListView.as_view(), name='user-list'),
    
# ]


from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
