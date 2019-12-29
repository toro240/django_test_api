from rest_framework import viewsets
from .models import Diary
from .serializer import DiarySerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
