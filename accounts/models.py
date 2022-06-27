from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from data.models import Lesson


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email является обязательным полем')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)

    is_premium = models.BooleanField('Премиум', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


THEMES = (
    (0, 'Светлая'),
    (1, 'Темная'),
)

FINGERING_STYLES = (
    (0, 'Вертикально'),
    (1, 'Горизонтально'),
)


class UserSettings(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользатель', related_name='settings', on_delete=models.CASCADE)
    theme = models.IntegerField('Цветовая тема', choices=THEMES, default=0)
    font_size = models.IntegerField('Размер шрифта', default=0)
    fingering_size = models.IntegerField('Размер аппликатуры', default=0)
    fingering_style = models.IntegerField('Стиль аппликатуры аккордов', choices=FINGERING_STYLES, default=0)

    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователя'


class UserProgress(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользатель', on_delete=models.CASCADE)
    favorite_lessons = models.ManyToManyField(Lesson, related_name="favorite_lessons",
                                              verbose_name="Избранные уроки и разборы", blank=True)
    complete_lessons = models.ManyToManyField(Lesson, related_name="complete_lessons",
                                              verbose_name="Пройденные уроки", blank=True)

    class Meta:
        verbose_name = 'Прогресс пользователя'
        verbose_name_plural = 'Прогресс пользователя'


@receiver(post_save, sender=User)
def add_details(sender, instance, created, **kwargs):
    if created:
        UserSettings.objects.update_or_create(user=instance)
        UserProgress.objects.update_or_create(user=instance)
