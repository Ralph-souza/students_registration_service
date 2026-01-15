import uuid

from factory.django import DjangoModelFactory
from django.utils import timezone

from apps.student.models import Student


class StudentFactory(DjangoModelFactory):
    id = str(uuid.uuid4())
    name = "fake_name"
    id_doc = "fake_doc"
    created_at = timezone.now()

    class Meta:
        model = Student
        