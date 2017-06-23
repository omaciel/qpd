"""Register admin modules here."""
from django.contrib import admin

from dashboard.models import OperatingSystem, Product, Release, TestRun


class TestRunAdmin(admin.ModelAdmin):
    """Hide some of the fields."""
    fields = [
        'name',
        'waved',
        'operating_system',
        'product',
        'release',
        'passed',
        'failed',
        'skipped',
        'error',
        'notes',
        ]

    list_display = (
        'release',
        'product',
        'operating_system',
        'name',
        'waved',
        'passed',
        'failed',
        'skipped',
        'error',
        'total',
        'total_executed',
        'percent_passed',
        'percent_failed',
        'percent_executed',
        'percent_not_executed',
        'notes',
    )


admin.site.register(OperatingSystem)
admin.site.register(Product)
admin.site.register(Release)
admin.site.register(TestRun, TestRunAdmin)
