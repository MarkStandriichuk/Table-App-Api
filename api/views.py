from rest_framework import viewsets
from .models import DataTable
from .serializers import DataTableSerializer


class DataTableViewSet(viewsets.ModelViewSet):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
