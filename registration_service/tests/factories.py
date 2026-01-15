import uuid

from factory.django import DjangoModelFactory
from factory import Faker, LazyFunction

from apps.registration.models import Registration


class RegistrationFactory(DjangoModelFactory):
    student_id = LazyFunction(lambda: uuid.uuid4())
    email = Faker('email')
    phone = Faker('phone_number')
    gender = "male"
    degree = "graduation"
    contact_name = Faker('name')
    contact_number = Faker('phone_number')
    relationship = "father"

    class Meta:
        model = Registration
