from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Scheme, Lesson, Sound, Addition, UpdateInfo,\
    Accord, StringsInfo


class StringsInfoInline(admin.TabularInline):
    model = StringsInfo
    extra = 1


@admin.register(Accord)
class AccordAdmin(admin.ModelAdmin):
    list_display = ('title', 'muz_title', 'note', 'order', 'bare')
    list_editable = ('muz_title', 'order', 'bare')
    list_filter = ('note', 'bare')
    inlines = [StringsInfoInline, ]


@admin.register(Scheme)
class LessonSchemeAdmin(admin.ModelAdmin):
    list_display = ('code', 'inscription', 'image')


@admin.register(Sound)
class SoundAdmin(MarkdownxModelAdmin):
    filter_horizontal = ('accords', 'schemes', 'accords')
    list_display = ('title',)


@admin.register(Addition)
class AdditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'video')
    list_filter = ('lesson',)
    list_editable = ('video',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_type', 'number', 'title')
    list_filter = ('lesson_type', )


@admin.register(UpdateInfo)
class UpdateInfoAdmin(admin.ModelAdmin):
    list_display = ('version',)
