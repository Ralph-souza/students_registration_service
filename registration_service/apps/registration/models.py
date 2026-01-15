from django.db import models

from .choices import GENDER_CHOICES, DEGREE_CHOICES, RELATIONSHIP_CHOICES


class Registration(models.Model):
    student_id = models.UUIDField(blank=False, null=False)
    email = models.EmailField(max_length=250, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default=None)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default=None)
    contact_name = models.CharField(max_length=200, default=None, blank=True, null=True)
    contact_number = models.CharField(
        max_length=15, default=None, blank=True, null=True
    )
    relationship = models.CharField(
        max_length=50, choices=RELATIONSHIP_CHOICES, default=None
    )

    class Meta:
        verbose_name = "Registration"

    def __str__(self):
        return self.email
