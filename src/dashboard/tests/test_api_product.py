"""Functional tests for Products via API."""
import json

from rest_framework import status
from django.test import Client
from django.urls import reverse
from dashboard.models import Product
from dashboard.serializers import ProductSerializer

import pytest


@pytest.fixture
def _client():
    """Get an instance of a REST client."""
    return Client()


@pytest.mark.django_db
def test_positive_get_products(_client):
    """Fetch all products."""
    Product.objects.create(name='Red Hat')
    response = _client.get(reverse('get_post_products'))
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_product_by_name(_client):
    """Fetch product by name."""
    my_prod = Product.objects.create(name='Red Hat')
    response = _client.get(
        reverse(
            'get_delete_update_product',
            kwargs={'pk': my_prod.pk}))
    prod = Product.objects.get(pk=my_prod.pk)
    serializer = ProductSerializer(prod)
    assert response.data == serializer.data
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_invalid_product(_client):
    """Fetch an invalid product by ID."""
    response = _client.get(
        reverse('get_delete_update_product', kwargs={'pk': 100000}))
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_positive_create_product(_client):
    response = _client.post(
        reverse('get_post_products'),
        data=json.dumps({"name": "Red Hat Satellite 6"}),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_negative_create_product(_client):
    response = _client.post(
        reverse('get_post_products'),
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_positive_update_product(_client):
    fedora = Product.objects.create(name='Fedora')
    response = _client.put(
        reverse(
            'get_delete_update_product',
            kwargs={'pk': fedora.pk}),
        data=json.dumps({"name": "CentOS"}),
        content_type='application/json'
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_positive_delete_product(_client):
    fedora = Product.objects.create(name='Fedora')
    response = _client.delete(
        reverse(
            'get_delete_update_product',
            kwargs={'pk': fedora.pk}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_negative_delete_product(_client):
    response = _client.delete(
        reverse('get_delete_update_product', kwargs={'pk': 10000}),)
    assert response.status_code == status.HTTP_404_NOT_FOUND
