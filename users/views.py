from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializer import (
    RegistrationSerializer,
    LoginSerializer,
    UserSerializer
)


User = get_user_model()


class RegistrationAPIView(generics.CreateAPIView):

    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['post']


class LoginAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class UserAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
