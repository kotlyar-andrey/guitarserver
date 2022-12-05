from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Lesson


class LessonTests(APITestCase):
    """
    Тестирование получения уроков и разборов
    """

    @classmethod
    def setUpTestData(cls):
        Lesson.objects.create(lesson_type=0,
                              number=1,
                              title="Test lesson",
                              video="https://www.youtube.com/watch?v=t-uDzm5VU28",
                              )
        Lesson.objects.create(lesson_type=1,
                              number=1,
                              title="Test how to play",
                              video="https://www.youtube.com/watch?v=t-uDzm5VU28",
                              start_lesson=1,
                              rating=2)

    def test_get_lessons(self):
        """Получение списка уроков"""
        url = reverse('lessons_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_lesson(self):
        """Получение урока и проверка его ключей.
        Для обычного урока всегда rating == 0 и start_lesson == None
        """
        url = reverse("lesson_view", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating'], 0)
        self.assertEqual(response.data['lesson_type'], 0)
        self.assertIsNone(response.data['start_lesson'])
        self.assertIn('pk', response.data)
        self.assertIn('number', response.data)
        self.assertIn('title', response.data)
        self.assertIn('video', response.data)
        self.assertIn('intro', response.data)
        self.assertIn('songs', response.data)
        self.assertIn('additions', response.data)

    def test_get_how_to_plays(self):
        """Получение списка разборов"""
        url = reverse('howtoplays_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_howtoplay(self):
        """Получение разбора и проверка его ключей"""
        url = reverse("howtoplay_view", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['lesson_type'], 1)
        self.assertIn('pk', response.data)
        self.assertIn('number', response.data)
        self.assertIn('title', response.data)
        self.assertIn('video', response.data)
        self.assertIn('intro', response.data)
        self.assertIn('songs', response.data)
        self.assertIn('additions', response.data)
        self.assertIn('start_lesson', response.data)
        self.assertIn('rating', response.data)
