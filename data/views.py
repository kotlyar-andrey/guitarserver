from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from . models import Lesson, Chord, Beat, UpdatedSubjects
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


def get_updated_data(user_version):
    updated_lessons = set()
    updated_howtoplays = set()
    updated_chords = set()
    updated_beats = set()
    latest_version = UpdatedSubjects.objects.latest('version').version
    for v in range(user_version + 1, latest_version + 1):
        try:
            update_info = UpdatedSubjects.objects.get(version=v)
            updated_lessons.update([item.pk for item in update_info.edited_lessons.all() if item.lesson_type == 0])
            updated_howtoplays.update([item.pk for item in update_info.edited_lessons.all() if item.lesson_type == 1])
            updated_chords.update([item.pk for item in update_info.edited_chords.all()])
            updated_beats.update([item.pk for item in update_info.edited_beats.all()])
        except:
            continue
    return {
        'lessons': updated_lessons,
        'howtoplays': updated_howtoplays,
        'chords': updated_chords,
        'beats': updated_beats,
        'last_version': latest_version
    }


class UpdateView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, version):
        updated_data = get_updated_data(version)
        return Response(updated_data,
                        status=status.HTTP_200_OK)


class VersionView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        latest_version = UpdatedSubjects.objects.latest('version').version
        return Response({'last_version': latest_version},
                        status=status.HTTP_200_OK)
