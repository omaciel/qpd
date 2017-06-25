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
    operating_system = serializers.PrimaryKeyRelatedField(
        queryset=OperatingSystem.objects.all())
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())
    release = serializers.PrimaryKeyRelatedField(
        queryset=Release.objects.all())

    # Additional fields
    total = serializers.SerializerMethodField()
    total_executed = serializers.SerializerMethodField()
    percent_passed = serializers.SerializerMethodField()
    percent_failed = serializers.SerializerMethodField()
    percent_executed = serializers.SerializerMethodField()
    percent_not_executed = serializers.SerializerMethodField()
    pqi = serializers.SerializerMethodField()

    def get_total(self, obj):
        """Generic SUM method."""
        return sum([obj.passed, obj.failed, obj.skipped, obj.error])

    def get_total_executed(self, obj):
        """Generic SUM method."""
        return sum([obj.passed, obj.failed])

    def get_percent_passed(self, obj):
        """Generic SUM method."""
        total_executed = self.get_total_executed(obj)
        return (
            (obj.passed / total_executed) * 100
            if total_executed > 0
            else 0)

    def get_percent_failed(self, obj):
        """Generic SUM method."""
        total_executed = self.get_total_executed(obj)
        return (
            (obj.failed / total_executed) * 100
            if total_executed > 0
            else 0)

    def get_percent_executed(self, obj):
        """Generic SUM method."""
        total = self.get_total(obj)
        total_executed = self.get_total_executed(obj)
        return (
            (obj.failed / total_executed) * 100
            if total > 0
            else 0)

    def get_percent_not_executed(self, obj):
        """Generic SUM method."""
        total = self.get_total(obj)
        return (
            (obj.skipped / total) * 100
            if total > 0
            else 0)

    def get_pqi(self, obj):
        """Generic SUM method."""
        total = self.get_total(obj)
        return obj.passed / total

    class Meta:
        model = TestRun
        fields = (
            'id',
            'name',
            'product',
            'release',
            'operating_system',
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
            'pqi',
            'notes',
        )
