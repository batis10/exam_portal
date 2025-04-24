from django.db import models
from django.conf import settings
from courses.models import Course
from exams.models import Exam

class Certificate(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='certificates'
    )
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.TextField()

    def __str__(self):
        return f"Certificate for {self.user.email} - {self.course.title}"

