"""Responsible for providing JSON output for REST calls."""
from rest_framework import serializers
from dashboard.models import (
    OperatingSystem,
    Product,
    Release,
    TestRun,
)


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


class TestRunSerializer(serializers.ModelSerializer):
    """Provide serialization for TestRun model."""
    operating_system = serializers.PrimaryKeyRelatedField(queryset=OperatingSystem.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    release = serializers.PrimaryKeyRelatedField(queryset=Release.objects.all())

    class Meta:
        model = TestRun
        fields = (
            'created_on',
            'error',
            'failed',
            'id',
            'notes',
            'operating_system',
            'passed',
            'percent_executed',
            'percent_failed',
            'percent_not_executed',
            'percent_passed',
            'product',
            'release',
            'skipped',
            'total',
            'total_executed',
            'updated_on',
            'waved',
            'name',
        )
