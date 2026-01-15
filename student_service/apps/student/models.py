import uuid

from django.db import models
from django.utils import timezone

class Student(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=200, blank=False, null=False)
    id_doc = models.CharField(max_length=15, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Student"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
