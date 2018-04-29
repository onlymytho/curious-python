from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Stock

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Stock.objects.all().order_by('gain_value')
    serializer_class = StockSerializers

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('market', )
    search_fields = ('stock_name', )

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
