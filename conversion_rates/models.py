from django.db import models


class ExchangeRateList(models.Model):
    """Exchange rate list contains daily exchange rates."""

    date_published = models.DateField()
    date_start = models.DateField()
    list_number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Tečajna lista'
        verbose_name_plural = 'Tečajne liste'

    def __str__(self):
        return '{}'.format(self.list_number)


class ExchangeRate(models.Model):
    """Exchange rate for a single currency on a date from the list."""

    er_list = models.ForeignKey(ExchangeRateList)
    currency = models.CharField(max_length=3)
    value = models.DecimalField(decimal_places=8, max_digits=14)

    def __str__(self):
        return '{} {}'.format(self.er_list.date_start, self.currency)