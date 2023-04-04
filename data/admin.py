from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Scheme, Lesson, Song, Addition, UpdatedSubjects,\
    Chord, StringsInfo, Strike, Beat


class StringsInfoInline(admin.TabularInline):
    model = StringsInfo
    extra = 1


@admin.register(Chord)
class AccordAdmin(admin.ModelAdmin):
    list_display = ('title', 'muz_title', 'note', 'order', 'bare')
    list_editable = ('muz_title', 'order', 'bare')
    list_filter = ('note', 'bare')
    inlines = [StringsInfoInline, ]


class StrikeInline(admin.TabularInline):
    model = Strike
    extra = 1


@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    list_display = ("inscription", 'code', 'duration')
    list_filter = ('beat_type',)
    inlines = [StrikeInline, ]


@admin.register(Scheme)
class LessonSchemeAdmin(admin.ModelAdmin):
    list_display = ('inscription', 'image')


@admin.register(Song)
class SongAdmin(MarkdownxModelAdmin):
    filter_horizontal = ('chords', 'schemes', 'beats')
    list_display = ('title', 'lesson', 'metronome')
    list_editable = ('metronome',)


@admin.register(Addition)
class AdditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'video')
    list_filter = ('lesson',)
    list_editable = ('video',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_type', 'number', 'title')
    list_filter = ('lesson_type', )



@admin.register(UpdatedSubjects)
class UpdateInfoAdmin(admin.ModelAdmin):
    list_display = ('version',)
