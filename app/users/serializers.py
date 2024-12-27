from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    register_username = serializers.EmailField()  # update to match form field name
    register_password = serializers.CharField(write_only=True)  # updated to match form field name
    location = serializers.CharField(max_length=255, required=False)

    def validate_register_username(self, value):  # updated to match form field name
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Email is already taken.")
        return value

    def validate_register_password(self, value):  # updated to match form field name
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value

    def validate_full_name(self, value):
        if len(value.split(' ', 1)) < 2:
            raise serializers.ValidationError("Please provide both first and last name.")
        return value

    def create(self, validated_data):
        full_name = validated_data.get('full_name')
        first_name, last_name = full_name.split(' ', 1) if ' ' in full_name else (full_name, '')

        password = validated_data.pop('register_password')  # updated to match form field name
        user = User.objects.create_user(
            username=validated_data.get('register_username'),  # updated to match form field name
            email=validated_data.get('register_username'),  # updated to match form field name
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        if validated_data.get('location'):
            user.location = validated_data.get('location')
            user.save()

        return user


class LoginSerializer(serializers.Serializer):
    login_username = serializers.EmailField()  # updated to match form field name
    login_password = serializers.CharField(write_only=True)  # updated to match form field name

    def validate(self, data):
        username = data.get('login_username')  # updated to match form field name
        password = data.get('login_password')  # updated to match form field name

        # Use Django's built-in authentication
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        
        return {
            'user': user
        }

