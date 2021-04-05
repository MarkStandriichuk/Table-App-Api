from django.db import models

class DataTable(models.Model):
    date = models.DateField(verbose_name='Date', auto_now=False)
    client_name = models.CharField(verbose_name='Client name', max_length=200)
    provider_name = models.CharField(verbose_name='Providers name', max_length=200)
    revenue = models.DecimalField(verbose_name='Revenue', max_digits=10, decimal_places=2)
    wons = models.IntegerField(verbose_name='Wons', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name