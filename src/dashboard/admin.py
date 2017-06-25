"""Register admin modules here."""
from django.contrib import admin

from dashboard.models import OperatingSystem, Product, Release, TestRun


admin.site.register(OperatingSystem)
admin.site.register(Product)
admin.site.register(Release)
admin.site.register(TestRun)
