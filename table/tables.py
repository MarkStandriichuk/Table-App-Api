import django_tables2 as tables
from api.models import DataTable

class MyTable(tables.Table):
    class Meta:
        model = DataTable
        template_name = "django_tables2/bootstrap.html"
        fields = ('date', 'client_name', 'provider_name', 'revenue', 'wons',)