from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Hero
class Heroserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name','alias')