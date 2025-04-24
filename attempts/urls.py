from django.urls import path
from .views import (
    ExamAttemptListCreateView,
    ExamAttemptDetailView,
    StudentAnswerListCreateView,
    StudentAnswerDetailView,
)

urlpatterns = [
    # Exam Attempts
    path('', ExamAttemptListCreateView.as_view(), name='exam-attempt-list-create'),
    path('<int:pk>/', ExamAttemptDetailView.as_view(), name='exam-attempt-detail'),

    # Student Answers (per attempt)
    path('<int:attempt_id>/answers/', StudentAnswerListCreateView.as_view(), name='student-answer-list-create'),
    path('answers/<int:pk>/', StudentAnswerDetailView.as_view(), name='student-answer-detail'),
]
