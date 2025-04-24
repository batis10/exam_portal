from django.urls import path
from .views import (
    QuestionListCreateView,
    QuestionDetailView,
    OptionListCreateView,
    OptionDetailView,
    TagListCreateView,
    TagDetailView,
    QuestionTagMapCreateView,
)

urlpatterns = [
    # Questions
    path('', QuestionListCreateView.as_view(), name='question-list-create'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),

    # Options
    path('<int:question_id>/options/', OptionListCreateView.as_view(), name='option-list-create'),
    path('options/<int:pk>/', OptionDetailView.as_view(), name='option-detail'),

    # Tags
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    # Tag Mapping
    path('<int:question_id>/tags/map/', QuestionTagMapCreateView.as_view(), name='question-tag-map'),
]
