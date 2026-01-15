import pytest

from .factories import StudentFactory

pytestmark = pytest.mark.django_db


class TestStudentModel:
    def test_string_conversion(self):
        student = StudentFactory(name="Fulano")

        assert "Fulano" == str(student)
        