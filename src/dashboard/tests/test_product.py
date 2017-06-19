"""Functional tests for all models."""
import pytest

from django.db.utils import IntegrityError

from dashboard.models import Product


@pytest.mark.django_db
@pytest.mark.parametrize('name', [
    'Red Hat Satellite 6',
    'Pulp',
    'Sonar',
])
def test_positive_create_product(name):
    """Created products has correct attributes."""
    Product.objects.create(name=name)
    my_prod = Product.objects.get(name=name)
    assert my_prod.name == name


@pytest.mark.django_db
def test_negative_create_product():
    """Cannot create products with same attributes."""
    Product.objects.create(name='Foo')
    with pytest.raises(IntegrityError):
            Product.objects.create(name='Foo')
