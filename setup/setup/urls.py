from django.contrib import admin
from django.urls import path, include
from empresa.views import EmpresasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('empresas', EmpresasViewSet, basename='Empresas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
