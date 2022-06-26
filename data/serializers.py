from rest_framework import serializers

from . models import Lesson, Sound, Addition, Accord, StringsInfo, Scheme


class StringInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringsInfo
        fields = ('pk', 'string', 'lad', 'number')


class AccordSerializer(serializers.ModelSerializer):
    lads = StringInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Accord
        fields = ('pk', 'title', 'muz_title', 'note', 'order', 'start_lad', 'bare', 'lads')


class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = ('pk', 'title', 'name', 'image')


class SoundSerializer(serializers.ModelSerializer):
    accords = AccordSerializer(many=True, read_only=True)
    schemes = SchemeSerializer(many=True, read_only=True)

    class Meta:
        model = Sound
        fields = ('pk', 'title', 'accords', 'schemes', 'text', 'metronome')


class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = ('pk', 'title', 'video', 'intro')


class LessonSerializer(serializers.ModelSerializer):
    sounds = SoundSerializer(many=True, read_only=True)
    additions = AdditionSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('pk', 'lesson_type', 'number', 'title', 'video',
                  'intro', 'sounds', 'additions', 'start_lesson', 'rating')
