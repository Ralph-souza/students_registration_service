import pytest

from .factories import RegistrationFactory

pytestmark = pytest.mark.django_db


class TestRegistrationModel:
    def test_string_conversion(self):
        registration = RegistrationFactory(email="test@example.com")

        assert "test@example.com" == str(registration)
