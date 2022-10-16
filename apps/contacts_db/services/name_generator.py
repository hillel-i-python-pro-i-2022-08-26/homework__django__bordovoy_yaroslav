from faker import Faker

fake = Faker()


def get_name() -> str:
    generated_name = fake.name()

    return generated_name
