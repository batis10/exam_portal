from rest_framework import generics
from .models import Question, Option,QuestionTagMap , QuestionTag
from .serializers import QuestionSerializer, OptionSerializer, QuestionTagSerializer, QuestionTagMapSerializer


# Questions
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Options
class OptionListCreateView(generics.ListCreateAPIView):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.filter(question_id=self.kwargs['question_id'])

    def perform_create(self, serializer):
        serializer.save(question_id=self.kwargs['question_id'])


class OptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


# Tags
class TagListCreateView(generics.ListCreateAPIView):
    queryset = QuestionTag.objects.all()
    serializer_class = QuestionTagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionTag.objects.all()
    serializer_class = QuestionTagSerializer


# Mapping tags to questions
class QuestionTagMapCreateView(generics.CreateAPIView):
    serializer_class = QuestionTagMapSerializer

    def perform_create(self, serializer):
        serializer.save(question_id=self.kwargs['question_id'])
