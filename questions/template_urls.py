from django.urls import path
from .template_view import QuestionListView  # Import your template view here
urlpatterns = [
    # Questions
    path('', QuestionListView.as_view(), name='question-list'),

]
