from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import OperatingSystem, Product, Release
from dashboard.serializers import OperatingSystemSerializer, ProductSerializer, ReleaseSerializer


# Operating System
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_operating_system(request, pk):
    try:
        my_op = OperatingSystem.objects.get(pk=pk)
    except OperatingSystem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single OperatingSystem
    if request.method == 'GET':
        serializer = OperatingSystemSerializer(my_op)
        return Response(serializer.data)
    # delete a single OperatingSystem
    elif request.method == 'DELETE':
        my_op.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single OperatingSystem
    elif request.method == 'PUT':
        serializer = OperatingSystemSerializer(my_op, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_operating_sytems(request):
    # get all Operating Systems
    if request.method == 'GET':
        ops = OperatingSystem.objects.all()
        serializer = OperatingSystemSerializer(ops, many=True)
        return Response(serializer.data)
    # insert a new record for a OperatingSystem
    if request.method == 'POST':
        data = {
            'family': request.data.get('family'),
            'major': int(request.data.get('major')),
            'minor': int(request.data.get('minor')),
            'patch': int(request.data.get('patch')),
        }
        serializer = OperatingSystemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Product
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_product(request, pk):
    try:
        my_op = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single Product
    if request.method == 'GET':
        serializer = ProductSerializer(my_op)
        return Response(serializer.data)
    # delete a single Product
    elif request.method == 'DELETE':
        my_op.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single Product
    elif request.method == 'PUT':
        serializer = ProductSerializer(my_op, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_products(request):
    # get all Products
    if request.method == 'GET':
        ops = Product.objects.all()
        serializer = ProductSerializer(ops, many=True)
        return Response(serializer.data)
    # insert a new record for a Product
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Release
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_release(request, pk):
    try:
        my_op = Release.objects.get(pk=pk)
    except Release.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single Release
    if request.method == 'GET':
        serializer = ReleaseSerializer(my_op)
        return Response(serializer.data)
    # delete a single Release
    elif request.method == 'DELETE':
        my_op.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single Release
    elif request.method == 'PUT':
        serializer = ReleaseSerializer(my_op, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_releases(request):
    # get all Releases
    if request.method == 'GET':
        ops = Release.objects.all()
        serializer = ReleaseSerializer(ops, many=True)
        return Response(serializer.data)
    # insert a new record for a Release
    if request.method == 'POST':
        data = {
            'major': int(request.data.get('major')),
            'minor': int(request.data.get('minor')),
            'patch': int(request.data.get('patch')),
        }
        serializer = ReleaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
