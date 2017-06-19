"""Functional tests for all models."""
import pytest

from django.db.utils import IntegrityError

from dashboard.models import Release


@pytest.mark.django_db
def test_positive_create_release():
    """Created releases has correct attributes."""
    Release.objects.create(
        major=7,
        minor=3,
        patch=0
    )
    my_release = Release.objects.get(major=7, minor=3, patch=0)
    assert my_release.major == 7
    assert my_release.minor == 3
    assert my_release.patch == 0


@pytest.mark.django_db
def test_negative_create_release():
    """Cannot create releases with same attributes."""
    Release.objects.create(
        major=7,
        minor=3,
        patch=0
    )
    with pytest.raises(IntegrityError):
            Release.objects.create(
                major=7,
                minor=3,
                patch=0
            )
