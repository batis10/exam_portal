from rest_framework import serializers
from .models import Feedback
from exams.serializers import ExamSerializer

class FeedbackSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'exam', 'rating', 'comments', 'created_at']
        read_only_fields = ['id', 'created_at']
