from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Mail


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = ['subject', 'body', 'receiver']

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.sender = self.context.get('request').user
        obj.save()
        return obj


class MailReadSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Mail
        fields = '__all__'
