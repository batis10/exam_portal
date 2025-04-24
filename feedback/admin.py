from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'exam', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('user__email', 'exam__title', 'comments')
    ordering = ('-created_at',)

