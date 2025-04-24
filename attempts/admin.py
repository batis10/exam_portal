from django.contrib import admin
from .models import ExamAttempt, StudentAnswer

@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'status', 'score', 'started_at', 'submitted_at')
    list_filter = ('status', 'exam')
    search_fields = ('user__email', 'exam__title')
    ordering = ('-started_at',)


@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt', 'question', 'selected_option', 'is_correct', 'marks_obtained')
    list_filter = ('is_correct',)
    search_fields = ('attempt__user__email', 'question__question_text')

