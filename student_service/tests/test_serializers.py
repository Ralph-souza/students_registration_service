import pytest

from rest_framework.test import RequestsClient

from apps.student.serializers import StudentSerializer
from .factories import StudentFactory

pytestmark = pytest.mark.django_db


class TestStudentSerializer:
    def test_serializer_read_only_fields(self, student_payload):
        student = StudentFactory()
        rc = RequestsClient()

        request = rc.post("http://127.0.0.1:8000/v1/api/student/", student_payload)
        response_data = eval(request.content)
        response_data["id"] == student.id
        response_data["created_at"] == student.created_at
        serializer = StudentSerializer(data=student_payload)

        assert serializer.is_valid() is True
        assert "id" not in serializer.validated_data
        assert "created_at" not in serializer.validated_data
