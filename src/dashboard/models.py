"""Models for the QPD application."""
from django.db import models


class OperatingSystem(models.Model):
    """Represents an Operating System."""
    major = models.PositiveIntegerField()
    minor = models.PositiveIntegerField()
    patch = models.PositiveIntegerField()
    family = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('family', 'major', 'minor', 'patch')

    def __str__(self):
        return str('{} {}.{}.{}'.format(
            self.family, self.major, self.minor, self.patch))

    def __unicode__(self):
        return str('{} {}.{}.{}'.format(
            self.family, self.major, self.minor, self.patch))


class Product(models.Model):
    """Represents a product."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str('{}'.format(self.name))

    def __unicode__(self):
        return str('{}'.format(self.name))


class Release(models.Model):
    """Represents a product release."""
    major = models.PositiveIntegerField()
    minor = models.PositiveIntegerField()
    patch = models.PositiveIntegerField()

    class Meta:
        unique_together = ('major', 'minor', 'patch')

    def __str__(self):
        return str('{}.{}.{}'.format(
            self.major, self.minor, self.patch))

    def __unicode__(self):
        return str('{}.{}.{}'.format(
            self.major, self.minor, self.patch))
