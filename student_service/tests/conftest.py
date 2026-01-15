import pytest

from .factories import StudentFactory


@pytest.fixture()
def student():
    return StudentFactory()


@pytest.fixture()
def student_payload():
    return {"id_doc": "some_doc_id", "name": "some_name"}


@pytest.fixture()
def student_payload_invalid():
    return {"id_doc": None, "name": "some_name"}