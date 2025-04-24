from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'instructor', 'created_at')
    list_filter = ('category', 'instructor')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'status', 'enrolled_at')
    list_filter = ('status',)
    search_fields = ('user__email', 'course__title')
    ordering = ('-enrolled_at',)

