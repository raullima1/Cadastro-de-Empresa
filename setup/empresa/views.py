from rest_framework import viewsets, generics
from empresa.models import Empresa
from empresa.serializer import EmpresaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EmpresasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as empresas"""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
