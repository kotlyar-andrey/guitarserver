from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from . models import Lesson, Accord, UpdateInfo
from . serializers import LessonSerializer, AccordSerializer


class LessonsList(generics.ListAPIView):
    queryset = Lesson.objects.filter(lesson_type=0)
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)


class LessonView(generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(lesson_type=0)
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)


class HowToPlayList(generics.ListAPIView):
    queryset = Lesson.objects.filter(lesson_type=1)
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)


class HowToPlayView(generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(lesson_type=1)
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)


class AccordsList(generics.ListAPIView):
    queryset = Accord.objects.all()
    serializer_class = AccordSerializer
    permission_classes = (AllowAny,)


class AccordView(generics.RetrieveAPIView):
    queryset = Accord.objects.all()
    serializer_class = AccordSerializer
    permission_classes = (AllowAny,)
