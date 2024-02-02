from rest_framework import routers
from .api import equipoViewSet

router = routers.DefaultRouter()

router.register('api/equipo', equipoViewSet, 'equipo')


urlpatterns = router.urls