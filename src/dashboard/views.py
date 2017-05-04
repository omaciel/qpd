from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import OperatingSystem
from dashboard.serializers import OperatingSystemSerializer


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
