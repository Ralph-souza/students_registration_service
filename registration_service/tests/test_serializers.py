import pytest
from unittest.mock import patch

from rest_framework.test import RequestsClient

from apps.registration.serializers import RegistrationSerializer
from .factories import RegistrationFactory

pytestmark = pytest.mark.django_db


class TestRegistrationSerializer:
    def test_serializer_read_only_fields(self, registration_payload):
        registration = RegistrationFactory()
        rc = RequestsClient()

        request = rc.post("http://127.0.0.1:8000/v1/api/registration/", registration_payload)
        response_data = eval(request.content)
        response_data["id"] == registration.id
        
        serializer = RegistrationSerializer(data=registration_payload)

        assert serializer.is_valid() is True
        assert "id" not in serializer.validated_data

    def test_serializer_validates_student_id_exists(self, registration_payload):
        """Testa que o serializer valida se o student_id existe"""
        with patch('apps.registration.serializers.validate_student_exists', return_value=True):
            serializer = RegistrationSerializer(data=registration_payload)
            assert serializer.is_valid() is True

    def test_serializer_validates_student_id_not_exists(self, registration_payload):
        """Testa que o serializer rejeita student_id inexistente"""
        with patch('apps.registration.serializers.validate_student_exists', return_value=False):
            serializer = RegistrationSerializer(data=registration_payload)
            assert serializer.is_valid() is False
            assert 'student_id' in serializer.errors

    def test_serializer_validates_email_format(self, registration_payload):
        """Testa validação de formato de email"""
        registration_payload["email"] = "invalid_email"
        with patch('apps.registration.serializers.validate_student_exists', return_value=True):
            serializer = RegistrationSerializer(data=registration_payload)
            assert serializer.is_valid() is False
            assert 'email' in serializer.errors
