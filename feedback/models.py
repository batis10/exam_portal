from django.db import models
from django.conf import settings
from exams.models import Exam

class Feedback(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.PositiveIntegerField()
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.email} for {self.exam.title}"

