from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from dashboard.models import (
    OperatingSystem,
    Product,
    Release,
    TestRun,
    )
from dashboard.serializers import (
    OperatingSystemSerializer,
    ProductSerializer,
    ReleaseSerializer,
    TestRunSerializer,
    )


# 'root' view
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'operating_systems': reverse(
            'operating_system_list', request=request, format=format),
        'products': reverse(
            'product_list', request=request, format=format),
        'releases': reverse(
            'release_list', request=request, format=format),
        'testruns': reverse(
            'testrun_list', request=request, format=format),
    })


class OperatingSystemList(generics.ListCreateAPIView):
    """ListCreateAPIView for OperatingSystem model."""
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class OperatingSystemDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView for OperatingSystem model."""
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class ProductList(generics.ListCreateAPIView):
    """ListCreateAPIView for Product model."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView for Product model."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReleaseList(generics.ListCreateAPIView):
    """ListCreateAPIView for Release model."""
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ReleaseDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView for Release model."""
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class TestRunList(generics.ListCreateAPIView):
    """ListCreateAPIView for TestRun model."""
    queryset = TestRun.objects.all()
    serializer_class = TestRunSerializer


class TestRunDetail(generics.RetrieveUpdateDestroyAPIView):
    """RetrieveUpdateDestroyAPIView for TestRun model."""
    queryset = TestRun.objects.all()
    serializer_class = TestRunSerializer
