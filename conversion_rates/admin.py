from django.contrib import admin
from django.db.models import Count
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

    date_hierarchy = 'date_start'

    search_fields = ('=list_number',)
    
    fieldsets = (
        (None, {
            'fields': (
                ('list_number', 'number_of_rates'),
                ('date_published', 'date_start'),
            )
        }),
    )
    readonly_fields = ('number_of_rates',)

    def number_of_rates(self, obj):
        return obj.ct
    number_of_rates.admin_order_field = 'ct'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.annotate(ct=Count('exchangerate'))
        return qs


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('er_list', 'list_date', 'currency', 'value')
    list_filter = ('currency',)

    def list_date(self, obj):
        return obj.er_list.date_start
    list_date.admin_order_field = 'er_list__date_start'
