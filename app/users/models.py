import uuid
from django.db import models

# class User(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     )
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     location = models.CharField(max_length=255, blank=True, null=True)
#     class Meta:
#         verbose_name = "user"
#         verbose_name_plural = "users"

#     def __str__(self):
#         return self.email
