"""Functional tests for all models."""

import pytest

from dashboard.models import OperatingSystem


@pytest.mark.django_db
def test_operatingsystem_attributes():
    """Created operating systems has correct attributes."""
    OperatingSystem.objects.create(
        family='Red Hat',
        major=7,
        minor=3,
        patch=0
    )
    my_op = OperatingSystem.objects.get(family='Red Hat')
    assert my_op.family == 'Red Hat'
