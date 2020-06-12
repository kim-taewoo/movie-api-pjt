from rest_framework import serializers
from django.conf import Settings

User = settins.AUTH_USER_MODEL

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )