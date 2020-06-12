from rest_framework import serializers
from django.conf import settings

User = settings.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )