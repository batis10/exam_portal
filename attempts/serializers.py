from rest_framework import serializers
from .models import ExamAttempt, StudentAnswer
from exams.serializers import ExamSerializer
from questions.serializers import QuestionSerializer, OptionSerializer

class ExamAttemptSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)

    class Meta:
        model = ExamAttempt
        fields = [
            'id', 'user', 'exam', 'started_at', 'submitted_at',
            'score', 'status', 'ip_address', 'browser_info', 'camera_snapshots'
        ]
        read_only_fields = ['id', 'started_at', 'submitted_at']


class StudentAnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    selected_option = OptionSerializer(read_only=True)

    class Meta:
        model = StudentAnswer
        fields = [
            'id', 'attempt', 'question', 'selected_option',
            'answer_text', 'is_correct', 'marks_obtained'
        ]
