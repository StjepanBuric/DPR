from django.contrib import admin
from .models import ExchangeRate, ExchangeRateList


class ExchangeRateInline(admin.TabularInline):
    """Administration inline interface for Exchange Rate."""

    model = ExchangeRate
    extra = 0
    max_num = 2


@admin.register(ExchangeRateList, )
class ExchangeRateListAdmin(admin.ModelAdmin):
    """Administration interface for Exchange Rate List."""

    inlines = [ExchangeRateInline]
    list_display = ('list_number', 'date_published',
                    'date_start', 'number_of_rates')

    def number_of_rates(self, obj):
        return obj.exchangerate_set.count()
