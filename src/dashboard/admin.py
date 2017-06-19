"""Register admin modules here."""
from django.contrib import admin

from dashboard.models import OperatingSystem, Product


admin.site.register(OperatingSystem)
admin.site.register(Product)
