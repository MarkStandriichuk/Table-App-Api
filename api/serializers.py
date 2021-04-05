from rest_framework import serializers
from .models import DataTable


class DataTableSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('date', 'client_name', 'provider_name', 'revenue', 'wons')
        model = DataTable