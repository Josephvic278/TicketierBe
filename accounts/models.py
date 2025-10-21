from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """A minimal, standard user model that inherits from Django's AbstractUser.

    Kept intentionally minimal to match a "very standard" user shape.
    If you later need extra fields (role, verified), add them with a new
    migration.
    """
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Device(models.Model):
    name = models.CharField(max_length=255)
    device_token = models.CharField(max_length=255, unique=True)
    last_seen_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
