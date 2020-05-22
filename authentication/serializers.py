from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import validators
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    email = serializers.EmailField(
        max_length=128,
        min_length=8,

    )

    first_name = serializers.CharField(
        max_length=128,
        min_length=2,
    )

    last_name = serializers.CharField(
        max_length=128,
        min_length=2,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'password', 'email']

    def validate(self, attrs):
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError({
                'email': ('Another user has already been registered under this email.')
            })
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    username = serializers.CharField(
        max_length=128,
        min_length=2,
    )

    class Meta:
        model = User
        fields = ['username', 'password']
