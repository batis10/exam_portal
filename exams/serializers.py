from rest_framework import serializers
from .models import Exam, ExamSettings
from courses.serializers import CourseSerializer

class ExamSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSettings
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    settings = ExamSettingsSerializer(read_only=True, source='examsettings')

    class Meta:
        model = Exam
        fields = [
            'id', 'course', 'title', 'description', 'duration_minutes',
            'total_marks', 'passing_marks', 'scheduled_at', 'max_attempts',
            'allow_backtracking', 'is_proctored', 'created_at', 'settings'
        ]
        read_only_fields = ['exam_id', 'created_at']
