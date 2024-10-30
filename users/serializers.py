from rest_framework import serializers

from users.models import MobileUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileUser
        fields = ('uuid',)

    def create(self, validated_data):
        user = MobileUser.objects.create(
            email=validated_data['uuid'],
        )
        user.save()

        return user
