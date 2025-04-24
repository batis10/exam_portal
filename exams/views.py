from rest_framework import generics
from .models import Exam, ExamSettings
from .serializers import ExamSerializer, ExamSettingsSerializer


class ExamListCreateView(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ExamSettingsRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'exam_id'
    queryset = ExamSettings.objects.all()
    serializer_class = ExamSettingsSerializer



















# from rest_framework import viewsets
# from .models import Exam, ExamSettings
# from .serializers import ExamSerializer, ExamSettingsSerializer
# from rest_framework.permissions import IsAuthenticated

# class ExamViewSet(viewsets.ModelViewSet):
#     queryset = Exam.objects.all()
#     serializer_class = ExamSerializer
#     permission_classes = [IsAuthenticated]


# class ExamSettingsViewSet(viewsets.ModelViewSet):
#     queryset = ExamSettings.objects.all()
#     serializer_class = ExamSettingsSerializer
#     permission_classes = [IsAuthenticated]

