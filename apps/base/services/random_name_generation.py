from faker import Faker

fake = Faker()


def generate_random_name() -> str:
    return fake.first_name()
