from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import AreaSerializer,ColorSerializer
# Create your views here.


@api_view(['GET'])
def get_areas(request):
    areas = Area.objects.all().prefetch_related('points','colors')
    res = []
    for area in areas:
        colors = area.colors.all()
        area_data = AreaSerializer(area, many=False).data
        for i in range(len(colors)):
            print(colors[i].fill_type)
            if colors[i].fill_type == "color":
                area_data['fill_type'] = colors[i].fill_type
                area_data['color'] = colors[0].color
            else:
                if colors.count()>1:
                    area_data['fill_type'] = colors[i].fill_type
                    area_data['color{}'.format(i)] = colors[i].color
                    area_data['angle'] = colors[i].angle
        res.append(area_data)
    return Response(res, status.HTTP_200_OK)





