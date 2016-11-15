from django.db import models


class ExchangeRateList(models.Model):
    """Exchange rate list contains daily exchange rates."""

    date_published = models.DateField()
    date_start = models.DateField()
    list_number = models.PositiveSmallIntegerField()


class ExchangeRate(models.Model):
    """Exchange rate for a single currency on a date from the list."""

    er_list = models.ForeignKey(ExchangeRateList)
    currency = models.CharField(max_length=3)
    value = models.DecimalField(decimal_places=8, max_digits=14)
