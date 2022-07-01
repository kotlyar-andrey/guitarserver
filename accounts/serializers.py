from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, UserProgress, UserSettings


class UserProgressSerializer(serializers.ModelSerializer):
    favorite_lessons = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    complete_lessons = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserProgress
        fields = ('favorite_lessons', 'complete_lessons',)


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ('theme', 'font_size', 'fingering_size', 'fingering_style',)


class UserSerializer(serializers.ModelSerializer):
    progress = UserProgressSerializer()
    settings = UserSettingsSerializer()

    class Meta:
        model = User
        fields = ('pk', 'email', 'is_premium', 'progress', 'settings',)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())]
                                   )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password, ])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
