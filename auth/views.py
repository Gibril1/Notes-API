from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer,  RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all
    serializer_class = RegisterSerializer

