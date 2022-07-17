from rest_framework import viewsets
from rest_framework import generics
from deshonnati_app.serializers import DailyFeedSerializer,DailyFeedSpecialBuldhanaSerializer,DailySpecialAkolaSerializer,AdvertisementFormSerializer
from .models import DailyFeed,DailySpecialAkola,DailySpecialBuldhana,AdvertisementForm
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import datetime

class DailyFeedViewsets(viewsets.ModelViewSet):
    def get_queryset(self):
        abc = DailyFeed.objects.filter(date=timezone.now().date()).order_by('city__name')
        return abc
    def get_serializer_class(self):
        return DailyFeedSerializer

class DailySpecialAkolaViewsets(viewsets.ModelViewSet):
    def get_queryset(self):
        abc = DailySpecialAkola.objects.filter(date=timezone.now().date())
        return abc
    def get_serializer_class(self):
        return DailySpecialAkolaSerializer

class DailySpecialBuldhanaViewsets(viewsets.ModelViewSet):
    def get_queryset(self):
        abc = DailySpecialBuldhana.objects.filter(date=timezone.now().date())
        return abc
    def get_serializer_class(self):
        return DailyFeedSpecialBuldhanaSerializer

class AdvertisementFormViewsets(viewsets.ModelViewSet):
    def get_queryset(self):
        abc = AdvertisementForm.objects.all()
        return abc
    def get_serializer_class(self):
        return AdvertisementFormSerializer
