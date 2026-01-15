import pytest
from unittest.mock import patch

from rest_framework.test import RequestsClient
from rest_framework import status

from apps.registration.models import Registration
from .factories import RegistrationFactory

pytestmark = pytest.mark.django_db


class TestRegistrationViewSet:
    def test_create_registration(self, registration_payload):
        rc = RequestsClient()
        request = rc.post("http://127.0.0.1:8000/v1/api/registration/", registration_payload)

        assert request.status_code == status.HTTP_201_CREATED
        assert Registration.objects.count() == 1

    def test_create_registration_fail(self, registration_payload_invalid):
        rc = RequestsClient()
        request = rc.post(
            "http://127.0.0.1:8000/v1/api/registration/", registration_payload_invalid
        )

        assert request.status_code == status.HTTP_400_BAD_REQUEST
        assert Registration.objects.count() == 0

    def test_create_registration_student_not_found(self, registration_payload):
        """Testa criação falha quando student_id não existe"""
        with patch('apps.registration.serializers.validate_student_exists', return_value=False):
            rc = RequestsClient()
            request = rc.post(
                "http://127.0.0.1:8000/v1/api/registration/", registration_payload
            )

            assert request.status_code == status.HTTP_400_BAD_REQUEST
            assert Registration.objects.count() == 0

    def test_update_registration(self, registration_payload):
        registration = RegistrationFactory()
        rc = RequestsClient()
        request = rc.put(
            f"http://127.0.0.1:8000/v1/api/registration/{registration.id}/",
            {
                "student_id": str(registration.student_id),
                "email": "updated@example.com",
                "phone": "9999999999",
                "gender": "female",
                "degree": "high_school",
            },
        )
        response_data = eval(request.content)

        assert request.status_code == status.HTTP_200_OK
        assert response_data["email"] == "updated@example.com"

    def test_list_registrations(self):
        RegistrationFactory.create_batch(3)
        rc = RequestsClient()
        request = rc.get("http://127.0.0.1:8000/v1/api/registration/")

        assert request.status_code == status.HTTP_200_OK

    def test_get_registration_by_id(self):
        registration = RegistrationFactory()
        rc = RequestsClient()
        request = rc.get(f"http://127.0.0.1:8000/v1/api/registration/{registration.id}/")

        assert request.status_code == status.HTTP_200_OK

    def test_delete_registration(self, registration_payload):
        rc = RequestsClient()
        request = rc.post("http://127.0.0.1:8000/v1/api/registration/", registration_payload)
        response_data = eval(request.content)
        r_exclude = rc.delete(
            f"http://127.0.0.1:8000/v1/api/registration/{response_data['id']}/"
        )

        assert r_exclude.status_code == status.HTTP_204_NO_CONTENT
        assert Registration.objects.count() == 0

    def test_by_student_endpoint(self):
        """Testa o endpoint customizado by_student"""
        import uuid
        student_id = uuid.uuid4()
        RegistrationFactory.create_batch(2, student_id=student_id)
        RegistrationFactory()  # Outro registro com student_id diferente
        
        rc = RequestsClient()
        request = rc.get(
            f"http://127.0.0.1:8000/v1/api/registration/by_student/?student_id={student_id}"
        )

        assert request.status_code == status.HTTP_200_OK
        response_data = eval(request.content)
        assert len(response_data) == 2
        assert all(str(reg["student_id"]) == str(student_id) for reg in response_data)

    def test_by_student_endpoint_missing_param(self):
        """Testa by_student sem parâmetro student_id"""
        rc = RequestsClient()
        request = rc.get("http://127.0.0.1:8000/v1/api/registration/by_student/")

        assert request.status_code == status.HTTP_400_BAD_REQUEST
