from django.urls import path

from . views import LessonsList, LessonView, HowToPlayList, HowToPlayView, AccordsList, AccordView

urlpatterns = [
    # get data:
    path('lessons/', LessonsList.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonView.as_view(), name='lesson_view'),
    path('howtoplays/', HowToPlayList.as_view(), name='howtoplays_list'),
    path('howtoplays/<int:pk>/', HowToPlayView.as_view(), name='howtoplay_view'),
    path('accords/', AccordsList.as_view(), name='accords_list'),
    path('accords/<int:pk>/', AccordView.as_view(), name='accord_view'),
]
