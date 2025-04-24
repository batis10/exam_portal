from django.db import models
from django.conf import settings
from exams.models import Exam
from questions.models import Question, Option

class ExamAttempt(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('graded', 'Graded'),
        ('invalidated', 'Invalidated')
    ]

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exam_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='attempts')
    started_at = models.DateTimeField()
    submitted_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    ip_address = models.CharField(max_length=45)
    browser_info = models.TextField()
    camera_snapshots = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.exam.title} ({self.status})"


class StudentAnswer(models.Model):
    
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)
    answer_text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    marks_obtained = models.IntegerField(default=0)

    def __str__(self):
        return f"Answer {self.answer_id} - Q{self.question.question_id} - Attempt {self.attempt.attempt_id}"

