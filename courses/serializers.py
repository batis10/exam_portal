from rest_framework import serializers
from .models import Course
from .models import Enrollment
from users.serializers import UserSerializer  # assuming instructor is a User

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'course_id', 'title', 'description', 'category',
            'instructor', 'image_url', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class EnrollmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at', 'status']
        read_only_fields = ['id', 'enrolled_at']


