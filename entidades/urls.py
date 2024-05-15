from django.urls import path, include
from rest_framework import routers
from .views import MaestroViewSet
from django.urls import include, re_path

router = routers.SimpleRouter()
router.register(r'maestros', MaestroViewSet,'maestros')

urlpatterns = [
    re_path(r"^", include(router.urls)),
]
