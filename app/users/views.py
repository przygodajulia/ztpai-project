from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer


class LoginRegisterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # For GET requests, render the login and register forms
        return render(request, 'users/login_register.html')

    def post(self, request, *args, **kwargs):
        action = request.data.get('action')
        if action == "register":
            return self.register_user(request)
        elif action == "login":
            return self.login_user(request)
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

    def register_user(self, request):
        register_serializer = RegisterSerializer(data=request.data)
        if register_serializer.is_valid():
            user = register_serializer.save()
            return Response({
                "message": "Registration successful! You can now log in."
            }, status=status.HTTP_201_CREATED)

        # If there are validation errors, return them in the response
        errors = [f"{error[0]}" for error in register_serializer.errors.values()]
        return Response({
            "errors": errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def login_user(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({
                "message": "Login successful!",
                "access_token": str(access_token)
            }, status=status.HTTP_200_OK)

        # If there are validation errors, return them in the response
        errors = [f"{error[0]}" for error in login_serializer.errors.values()]
        return Response({
            "errors": errors
        }, status=status.HTTP_400_BAD_REQUEST)
