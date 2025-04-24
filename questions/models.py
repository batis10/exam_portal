from django.db import models
from exams.models import Exam

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('mcq', 'Multiple Choice'),
        ('true_false', 'True/False'),
        ('short_answer', 'Short Answer'),
        ('long_answer', 'Long Answer')
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ]

    
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    media_url = models.TextField(null=True, blank=True)
    marks = models.IntegerField()

    def __str__(self):
        return f"Q{self.id}: {self.question_text[:50]}"


class Option(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Option {self.id} for Q{self.id}"


class QuestionTag(models.Model):
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class QuestionTagMap(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='tag_maps')
    tag = models.ForeignKey(QuestionTag, on_delete=models.CASCADE, related_name='tag_maps')

    class Meta:
        unique_together = ('question', 'tag')

    def __str__(self):
        return f"{self.question} <-> {self.tag}"

