from django.urls import path
from .views import (
    ExamListCreateView,
    ExamDetailView,
    ExamSettingsRetrieveUpdateView,
)

urlpatterns = [
    # Exams
    path('', ExamListCreateView.as_view(), name='exam-list-create'),
    path('<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),

    # Exam Settings (one-to-one with Exam)
    path('<int:exam_id>/settings/', ExamSettingsRetrieveUpdateView.as_view(), name='exam-settings'),
]
