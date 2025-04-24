from rest_framework import generics
from .models import ExamAttempt, StudentAnswer
from .serializers import ExamAttemptSerializer, StudentAnswerSerializer


# Exam Attempts
class ExamAttemptListCreateView(generics.ListCreateAPIView):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer


class ExamAttemptDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer


# Student Answers
class StudentAnswerListCreateView(generics.ListCreateAPIView):
    serializer_class = StudentAnswerSerializer

    def get_queryset(self):
        return StudentAnswer.objects.filter(attempt_id=self.kwargs['attempt_id'])

    def perform_create(self, serializer):
        serializer.save(attempt_id=self.kwargs['attempt_id'])


class StudentAnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer
