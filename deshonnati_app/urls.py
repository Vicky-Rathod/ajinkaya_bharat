from django.urls import include, path
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
# router.register(r'abcdeapi', viewsets.DailyFeedViewsets, basename='dailyfeed')
# router.register(r'abcdespecialapi', viewsets.DailySpecialAkolaViewsets, basename='dailyfeedakola')
# router.register(r'abcdespecialbuldhanaapi', viewsets.DailySpecialBuldhanaViewsets, basename='dailyfeedakola')
router.register(r'advformapi', viewsets.AdvertisementFormViewsets, basename='advform')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]