"""Functional tests for views."""
import json

from rest_framework import status
from django.test import Client
from django.urls import reverse
from dashboard.models import OperatingSystem
from dashboard.serializers import OperatingSystemSerializer

import pytest


invalid_payload = {
    'family': '',
    'major': 25,
    'minor': 0,
    'patch': 0,
}
valid_payload = {
    'family': 'Fedora',
    'major': 25,
    'minor': 0,
    'patch': 0,
}


@pytest.fixture
def _client():
    """Get an instance of a REST client."""
    return Client()


@pytest.mark.django_db
def test_get_operating_system(_client):
    OperatingSystem.objects.create(
        family='Red Hat',
        major=7,
        minor=3,
        patch=0
    )
    response = _client.get(reverse('get_post_operating_systems'))
    ops = OperatingSystem.objects.all()
    serializer = OperatingSystemSerializer(ops, many=True)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_operating_system_by_name(_client):
    """Fetch operating system by name."""
    my_op = OperatingSystem.objects.create(
        family='Red Hat',
        major=7,
        minor=3,
        patch=0
    )
    response = _client.get(
        reverse(
            'get_delete_update_operating_system',
            kwargs={'pk': my_op.pk}))
    op = OperatingSystem.objects.get(pk=my_op.pk)
    serializer = OperatingSystemSerializer(op)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_invalid_operating_system(_client):
    response = _client.get(
        reverse('get_delete_update_operating_system', kwargs={'pk': 100000}))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_positive_create_operating_system(_client):
    response = _client.post(
        reverse('get_post_operating_systems'),
        data=json.dumps(valid_payload),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_negative_create_operating_system(_client):
    response = _client.post(
        reverse('get_post_operating_systems'),
        data=json.dumps(invalid_payload),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_positive_update_operating_system(_client):
    fedora = OperatingSystem.objects.create(
        family='Fedora',
        major=24,
        minor=1,
        patch=0
    )
    response = _client.put(
        reverse(
            'get_delete_update_operating_system',
            kwargs={'pk': fedora.pk}),
        data=json.dumps(valid_payload),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_negative_update_operating_system(_client):
    fedora = OperatingSystem.objects.create(
        family='Fedora',
        major=22,
        minor=0,
        patch=1
    )
    response = _client.put(
        reverse(
            'get_delete_update_operating_system',
            kwargs={'pk': fedora.pk}),
        data=json.dumps(invalid_payload),
        content_type='application/json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_positive_delete_operating_system(_client):
    fedora = OperatingSystem.objects.create(
        family='Fedora',
        major=22,
        minor=0,
        patch=1
    )
    response = _client.delete(
        reverse(
            'get_delete_update_operating_system',
            kwargs={'pk': fedora.pk}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_negative_delete_operating_system(_client):
    response = _client.delete(
        reverse('get_delete_update_operating_system', kwargs={'pk': 10000}),)
    assert response.status_code == status.HTTP_404_NOT_FOUND
