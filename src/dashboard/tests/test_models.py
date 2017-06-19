"""Functional tests for all models."""
import pytest

from django.db.utils import IntegrityError

from dashboard.models import OperatingSystem


@pytest.mark.django_db
def test_positive_create_operating_system():
    """Created operating systems has correct attributes."""
    OperatingSystem.objects.create(
        family='Red Hat',
        major=7,
        minor=3,
        patch=0
    )
    my_op = OperatingSystem.objects.get(family='Red Hat')
    assert my_op.family == 'Red Hat'


@pytest.mark.django_db
def test_negative_create_operating_system():
    """Cannot create operating systems with same attributes."""
    OperatingSystem.objects.create(
        family='Red Hat',
        major=7,
        minor=3,
        patch=0
    )
    with pytest.raises(IntegrityError):
            OperatingSystem.objects.create(
                family='Red Hat',
                major=7,
                minor=3,
                patch=0
            )
