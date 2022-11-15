from typing import Iterator

from apps.contacts_db.models import Contacts
from . import date_of_birth_generator, name_generator, phone_number_generator


def data_for_db(amount: int) -> Iterator[Contacts]:
    for _ in range(amount):
        name = name_generator.get_name()
        phone_number = phone_number_generator.get_phone()
        date_of_birth = date_of_birth_generator.get_data_of_birth()

        yield Contacts(
            name=name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
