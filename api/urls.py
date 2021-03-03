from django.urls import path
from .views import get_areas
urlpatterns = [
    path('/areas', get_areas),
]