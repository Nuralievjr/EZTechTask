from rest_framework import serializers
from .models import *

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('lat', 'long')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('fill_type', 'color', 'angle' )

class AreaSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True)
    class Meta:
        model = Area
        fields = ('id', 'name', 'description', 'points')


