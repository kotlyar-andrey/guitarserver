from django.urls import path

from . views import LessonsList, LessonView, HowToPlayList, HowToPlayView, AccordsList, AccordView, BeatsList, \
    BeatView, UpdateView, VersionView, SimpleLessonsList, FullLessonView, SimpleHowToPlayList, FullHowToPlayView


urlpatterns = [
    # get data:
    path('lessons/', LessonsList.as_view(), name='lessons_list'),
    path('lessons/simple', SimpleLessonsList.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonView.as_view(), name='lesson_view'),
    path('lessons/<int:pk>/full', FullLessonView.as_view(), name='lesson_view'),

    path('howtoplays/', HowToPlayList.as_view(), name='howtoplays_list'),
    path('howtoplays/simple', SimpleHowToPlayList.as_view(), name='howtoplays_list'),
    path('howtoplays/<int:pk>/', HowToPlayView.as_view(), name='howtoplay_view'),
    path('howtoplays/<int:pk>/full', FullHowToPlayView.as_view(), name='howtoplay_view'),

    path('chords/', AccordsList.as_view(), name='accords_list'),
    path('chords/<int:pk>/', AccordView.as_view(), name='accord_view'),

    path('beats/', BeatsList.as_view(), name='beats_list'),
    path('beats/<int:pk>/', BeatView.as_view(), name='beat_view'),

    path('update/', VersionView.as_view(), name='version_view'),
    path('update/<int:version>/', UpdateView.as_view(), name='update_view')
]
