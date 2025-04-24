from django.db import models
from courses.models import Course

class Exam(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='exams'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()
    scheduled_at = models.DateTimeField()
    max_attempts = models.PositiveIntegerField()
    allow_backtracking = models.BooleanField(default=False)
    is_proctored = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"


class ExamSettings(models.Model):
    exam = models.OneToOneField(
        Exam,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='settings'
    )
    allow_negative_marking = models.BooleanField(default=False)
    negative_mark_per_wrong = models.FloatField(default=0.0)
    shuffle_questions = models.BooleanField(default=False)
    shuffle_options = models.BooleanField(default=False)
    allow_resume = models.BooleanField(default=False)
    camera_required = models.BooleanField(default=False)

    def __str__(self):
        return f"Settings for {self.exam.title}"

