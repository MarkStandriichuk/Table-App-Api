from django.views.generic import ListView
from django_tables2 import SingleTableView
from api.models import DataTable
from .tables import MyTable

class TableListView(SingleTableView):
    model = DataTable
    table_class = MyTable
    template_name = 'table.html'