from rest_framework import serializers
from .models import Certificate
from courses.serializers import CourseSerializer
from exams.serializers import ExamSerializer

class CertificateSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    exam = ExamSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = [
            'id', 'user', 'course', 'exam',
            'issued_at', 'certificate_url'
        ]
        read_only_fields = ['id', 'issued_at']
