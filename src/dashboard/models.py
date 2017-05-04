"""Models for the QPD application."""
from django.db import models


class OperatingSystem(models.Model):
    """Represents an Operating System."""
    major = models.PositiveIntegerField()
    minor = models.PositiveIntegerField()
    patch = models.PositiveIntegerField()
    family = models.CharField(max_length=50)

    def __str__(self):
        return str('{} {}.{}.{}'.format(
            self.family, self.major, self.minor, self.patch))

    def __unicode__(self):
        return str('{} {}.{}.{}'.format(
            self.family, self.major, self.minor, self.patch))
