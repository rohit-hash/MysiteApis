from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import Heroserializers
from .models import Hero 

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = Heroserializers
