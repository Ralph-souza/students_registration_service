import pytest
import uuid
from unittest.mock import patch

from .factories import RegistrationFactory


@pytest.fixture()
def registration():
    return RegistrationFactory()


@pytest.fixture()
def registration_payload():
    return {
        "student_id": str(uuid.uuid4()),
        "email": "test@example.com",
        "phone": "1234567890",
        "gender": "male",
        "degree": "graduation",
        "contact_name": "John Doe",
        "contact_number": "9876543210",
        "relationship": "father"
    }


@pytest.fixture()
def registration_payload_invalid():
    return {
        "student_id": str(uuid.uuid4()),
        "email": "invalid_email",  # Email inválido
        "phone": "",  # Phone vazio
        "gender": "invalid_gender",  # Gender inválido
    }


@pytest.fixture()
def registration_payload_minimal():
    """Payload mínimo com apenas campos obrigatórios"""
    return {
        "student_id": str(uuid.uuid4()),
        "email": "minimal@example.com",
        "phone": "1234567890",
    }


@pytest.fixture(autouse=True)
def mock_validate_student():
    """Mock automático para validate_student_exists em todos os testes"""
    # Patch no serializer onde a função é realmente usada
    with patch('apps.registration.serializers.validate_student_exists', return_value=True):
        yield
