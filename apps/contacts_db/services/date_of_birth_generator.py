import datetime

from faker import Faker

fake = Faker()


def get_data_of_birth() -> datetime.date:

    return fake.date_between("-50y", "today")
