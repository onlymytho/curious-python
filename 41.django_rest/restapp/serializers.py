# Serializers는 API에서 보여줄 정보들을 정의하는 파일
from .models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model

class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None, use_url = True)
    class Meta:
        model = Task
        fields = (
            'id',
            'task_name',
            'task_desc',
            'task_author',
            'completed',
            'date_created',
            'image'
            )

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
