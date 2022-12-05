from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from . models import Lesson, Chord, UpdateInfo
from . serializers import LessonSerializer, ChordSerializer


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
    queryset = Chord.objects.all()
    serializer_class = ChordSerializer
    permission_classes = (AllowAny,)


class AccordView(generics.RetrieveAPIView):
    queryset = Chord.objects.all()
    serializer_class = ChordSerializer
    permission_classes = (AllowAny,)
