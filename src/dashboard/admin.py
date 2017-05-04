"""Register admin modules here."""
from django.contrib import admin

from dashboard.models import OperatingSystem


admin.site.register(OperatingSystem)
