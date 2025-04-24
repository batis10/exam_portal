from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'exam', 'issued_at')
    search_fields = ('user__email', 'course__title', 'exam__title')
    ordering = ('-issued_at',)

