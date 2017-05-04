"""Responsible for providing JSON output for REST calls."""
from rest_framework import serializers
from dashboard.models import OperatingSystem


class OperatingSystemSerializer(serializers.ModelSerializer):
    """Provide serialization for OperatingSystem model."""
    class Meta:
        model = OperatingSystem
        fields = ('id', 'family', 'major', 'minor', 'patch',)
