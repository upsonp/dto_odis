from rest_framework.routers import DefaultRouter

from .views import MPAZonesViewSet, MPAZonesWithTimeseriesViewSet, SpeciesViewSet

router = DefaultRouter()
router.register(r'mpas', MPAZonesViewSet)
router.register(r'mpas-with-timeseries', MPAZonesWithTimeseriesViewSet, basename='mpas-with-timeseries')
router.register(r'species', SpeciesViewSet, basename='species')
