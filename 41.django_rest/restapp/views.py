from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Task

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('completed', )
    ordering = ('-date_created', )
    search_fields = ('task_name', )

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
