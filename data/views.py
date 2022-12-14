from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from . models import Lesson, Chord, Beat, UpdateInfo
from . serializers import LessonSerializer, ChordSerializer, BeatSerializer


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

class BeatsList(generics.ListAPIView):
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = (AllowAny,)


class BeatView(generics.RetrieveAPIView):
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer
    permission_classes = (AllowAny,)
