# Serializers는 API에서 보여줄 정보들을 정의하는 파일
from .models import Stock
from rest_framework import serializers
from django.contrib.auth import get_user_model

class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            "id",
            "stock_name",
            "market",
            "gain_value",
            "sell_value"
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
        fields = (
            "id",
            "username",
            "password"
            )
