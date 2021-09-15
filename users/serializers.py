from django.contrib.auth.models import User
from rest_framework import serializers
import re

from users.models import EmailUser


class EmailUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = EmailUser
        fields = ['id', 'username', 'password', 'email_address', 'contacts']

    def validate_email_address(self, value):
        if re.match("^[\w\.]+$", value):
            return value
        raise serializers.ValidationError("invalid email address")

    def create(self, validated_data):
        validated_data['email_address'] += '@amirrzw.com'
        obj = super().create(validated_data)
        obj.set_password(validated_data['password'])
        obj.save()
        return obj

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
