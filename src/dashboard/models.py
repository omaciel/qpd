"""Models for the QPD application."""
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


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


class TestRun(models.Model):
    """Represents a Test Run for a product release."""
    name = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    waved = models.BooleanField(default=False)
    # Foreign keys
    operating_system = models.ForeignKey(
        OperatingSystem, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    release = models.ForeignKey(
        Release, on_delete=models.CASCADE)

    passed = models.IntegerField()
    failed = models.IntegerField()
    skipped = models.IntegerField()
    error = models.IntegerField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str('{}'.format(self.name))

    def __unicode__(self):
        return str('{}'.format(self.name))

    def update_testrun_stats(self):

        self.total = sum([self.passed, self.failed, self.skipped, self.error])
        self.total_executed = sum([self.passed, self.failed])
        self.percent_passed = (
            (self.passed / float(self.total_executed)) * 100
            if self.total_executed > 0
            else 0)
        self.percent_failed = (
            (self.failed / float(self.total_executed)) * 100
            if self.total_executed > 0
            else 0)
        self.percent_executed = (
            (self.total_executed / float(self.total)) * 100
            if self.total > 0
            else 0)
        self.percent_not_executed = (
            (self.skipped / float(self.total)) * 100 if self.total > 0 else 0)
