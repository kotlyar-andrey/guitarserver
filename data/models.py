from django.db import models
from markdownx.models import MarkdownxField


LESSON_TYPES = (
    (0, 'Урок'),
    (1, 'Разбор'),
)

NOTE_DURATIONS = (
    (0, '1'),
    (1, '1/2'),
    (2, '1/4'),
    (3, '1/8'),
    (4, '1/16'),
    (5, '1/32'),
)

ALLOWED_STRIKES = (
    ('down', 'Вниз'),
    ('up', 'Вверх'),
    ('x', 'Щелчок'),
    ('pause', 'Пауза')
)


class Lesson(models.Model):
    """
    Главная модель данных для уроков и разборов.
    lesson_type отпределяет, урок это или разбор.
    """
    lesson_type = models.IntegerField("Вид урока", choices=LESSON_TYPES)
    number = models.IntegerField("Номер")
    title = models.CharField("Название", max_length=200)
    video = models.URLField("Видео", max_length=200)
    start_lesson = models.IntegerField("Подходит для урока № ", blank=True, null=True)
    intro = models.IntegerField("Длительность интро", default=0)
    rating = models.IntegerField("Рейтинг", default=0)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("number",)

    def __str__(self):
        if self.lesson_type == 0:
            return f"Урок № {self.number}. {self.title}"
        else:
            return f"Разбор № {self.number}. {self.title}"


class Chord(models.Model):
    """
    Основная информация об аккорде
    """
    title = models.CharField("Название", max_length=50)
    muz_title = models.CharField("Музыкальное название", max_length=20, blank=True, null=True)
    note = models.CharField("Нота", max_length=50, blank=True, null=True)
    order = models.IntegerField("Номер для сортировки", default=1)
    start_lad = models.IntegerField("С какого лада начинается", default=1)
    bare = models.BooleanField("Есть баре?", default=False)

    @property
    def code(self):
        res = self.title
        for lad in self.lads.all():
            res += f'_{lad.string}{lad.lad}'
        return res


    class Meta:
        verbose_name = "Аккорд"
        verbose_name_plural = "Аккорды"
        ordering = ("note", "order")

    def __str__(self):
        return self.title if not self.bare else f'{self.title} bare'


class StringsInfo(models.Model):
    """
    Информация о том, какая струна на каком ладу и каким польцем зажата
    для аккорда accord
    """
    accord = models.ForeignKey(Chord, on_delete=models.CASCADE, verbose_name="Аккорд", related_name="lads")
    string = models.IntegerField(default=1, verbose_name="Номер струны")
    lad = models.IntegerField(default=0, verbose_name="На каком ладу зажата",
                              help_text="-1 - не играется, 0 - открытая, 1-12 - номер лада")
    number = models.IntegerField(default=0, verbose_name="Каким пальцем",
                                 help_text="1-указательный, 2-средний, 3-безимянный, 4-мизинец")

    class Meta:
        verbose_name = "Струна"
        verbose_name_plural = "Струны"
        ordering = ("string",)


class Scheme(models.Model):
    """
    Схематический рисунок гитарного боя
    или другая схема для урока/разбора в виде ресунка
    """
    code = models.CharField("Кодовое название", help_text="Позволяет указать, для какого именно урока этот рисунок",
                            max_length=20, blank=True)
    inscription = models.CharField("Надпись", max_length=100, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to='lesson_schemes/',
                              height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = "Бой или схема (рисунок)"
        verbose_name_plural = "Бои или схемы (рисунки)"

    def __str__(self):
        return f"{self.code} - {self.inscription}"


class Beat(models.Model):
    """
    Класс, который хранит информацию об интерактивных боях.
    Например, бой № 1 (четверка), будет записан как ['down', 'up', 'x', 'up'], duration = 2
    """
    code = models.CharField("Кодовое название", help_text="Позволяет указать, для какого именно урока этот бой",
                            max_length=20, blank=True)
    inscription = models.CharField("Надпись", max_length=100, blank=True, null=True)
    duration = models.IntegerField("Длительность", choices=NOTE_DURATIONS)

    class Meta:
        verbose_name = "Интерактивный ритмический рисунок"
        verbose_name_plural = "Интерактивные ритмические рисунки"

    def __str__(self):
        return f"{self.code} - {self.inscription} - duration {self.duration}"


class Strike(models.Model):
    """
    Вид удара
    """
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE, verbose_name="Ритмический рисунок", related_name="strikes")
    strike = models.CharField(verbose_name="Удар", max_length=30, choices=ALLOWED_STRIKES)

    class Meta:
        verbose_name = "Удар"
        verbose_name_plural = "Удары"

    def __str__(self):
        return self.strike


class Song(models.Model): # TODO: rename to Song
    """
    Основной класс для песни, не зависимо от того, урок это или разбор.
    Содержит текст с markdown разметкой для отображения аккордов
    а также используемые ритмические бои и аккорды
    """
    lesson = models.ForeignKey(Lesson, verbose_name="Песня к...",
                               on_delete=models.CASCADE, related_name="songs")
    title = models.CharField("Название", max_length=200)
    chords = models.ManyToManyField(Chord, verbose_name="Аккорды", blank=True)
    schemes = models.ManyToManyField(
        Scheme, verbose_name="Ритмические рисунки (изображения)", blank=True)
    beats = models.ManyToManyField(Beat, verbose_name="Интерактивные ритмические рисунки", blank=True)
    text = MarkdownxField("Текст песни", help_text="С аккордами и переносами строк")
    metronome = models.IntegerField("Метроном", default=0)

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return self.title


class Addition(models.Model):
    """
    Дополнение к уроку или разбору: дополнительное видео с пояснениями
    """
    lesson = models.ForeignKey(Lesson, verbose_name="К уроку",
                               on_delete=models.CASCADE, related_name="additions")
    title = models.CharField("Название", max_length=200)
    video = models.URLField("Видео", max_length=200)
    intro = models.IntegerField("Длительность интро", default=0)

    class Meta:
        verbose_name = "Дополнение к уроку"
        verbose_name_plural = "Дополнения к уроку"

    def __str__(self):
        return self.title


class UpdateInfo(models.Model):
    """
    Содержит информацию о том, какие уроки или аккорды были изменены,
    а также версию данных.
    Используется для отслеживания изменений в уроках или аккордах.
    """
    version = models.IntegerField("Версия данных", default=0)
    editedLessons = models.ManyToManyField(
        Lesson, verbose_name="Измененные уроки", blank=True)
    editedAccords = models.ManyToManyField(
        Chord, verbose_name="Измененные аккорды", blank=True)

    class Meta:
        verbose_name = "Информация об обновлении"
        verbose_name_plural = "Информация об обновлении"
        ordering = ("-version",)

    def __str__(self):
        return str(self.version)
