from rest_framework import serializers

from . models import Lesson, Song, Addition, Chord, StringsInfo, Scheme, Strike, Beat


class StringInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringsInfo
        fields = ('pk', 'string', 'lad', 'number')


class ChordSerializer(serializers.ModelSerializer):
    lads = StringInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Chord
        fields = ('pk', 'title', 'muz_title', 'note', 'order', 'start_lad', 'bare', 'lads', 'code')


class BeatSerializer(serializers.ModelSerializer):
    strikes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Beat
        fields = ('pk', 'inscription', 'duration', 'strikes',)


class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = ('pk', 'inscription', 'image')


class SongSerializer(serializers.ModelSerializer):
    chords = ChordSerializer(many=True, read_only=True)
    schemes = SchemeSerializer(many=True, read_only=True)
    beats = BeatSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = ('pk', 'title', 'chords', 'schemes', 'beats', 'text', 'metronome')


class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addition
        fields = ('pk', 'title', 'video', 'intro')


class LessonSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    additions = AdditionSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('pk', 'lesson_type', 'number', 'title', 'video',
                  'intro', 'songs', 'additions', 'start_lesson', 'rating')
