# models.py
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    location = models.CharField(max_length=255, blank=True, null=True)

    username = models.EmailField(unique=True)

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username