from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Mail


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail
        fields = '__all__'
        read_only_fields = ['sender', 'sent_at', ]

    def validate_receiver(self, value):
        if self.context.get('request').user == value:
            raise serializers.ValidationError("enter another email address")
        else:
            return value

    def create(self, validated_data):
        validated_data['sender'] = self.context.get('request').user
        obj = super().create(validated_data)
        obj.save()
        return obj


class MailReadSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Mail
        fields = '__all__'
