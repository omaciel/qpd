"""Responsible for providing JSON output for REST calls."""
from rest_framework import serializers
from dashboard.models import OperatingSystem, Product, Release


class OperatingSystemSerializer(serializers.ModelSerializer):
    """Provide serialization for OperatingSystem model."""
    class Meta:
        model = OperatingSystem
        fields = ('id', 'family', 'major', 'minor', 'patch',)


class ProductSerializer(serializers.ModelSerializer):
    """Provide serialization for Product model."""
    class Meta:
        model = Product
        fields = ('id', 'name',)


class ReleaseSerializer(serializers.ModelSerializer):
    """Provide serialization for Release model."""
    class Meta:
        model = Release
        fields = ('id', 'major', 'minor', 'patch',)
