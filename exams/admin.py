from django.contrib import admin
from .models import Exam, ExamSettings

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'scheduled_at', 'max_attempts', 'is_proctored')
    list_filter = ('is_proctored', 'allow_backtracking')
    search_fields = ('title', 'course__title')
    ordering = ('-scheduled_at',)


@admin.register(ExamSettings)
class ExamSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'exam',
        'allow_negative_marking',
        'negative_mark_per_wrong',
        'shuffle_questions',
        'shuffle_options',
        'allow_resume',
        'camera_required'
    )
    list_filter = ('shuffle_questions', 'camera_required')

