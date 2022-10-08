import random
from string import ascii_letters, digits
import secrets


def number_of_signs(number: int | None) -> int:
    if number is None:
        number = random.randint(8, 20)
    return number


def passwords(amount: int) -> list[str]:
    passwords_for_view = []
    number_of_characters = number_of_signs(number=None)
    password_values = ascii_letters + digits
    for _ in range(amount):
        passwords_for_view.append(
            "".join(
                secrets.choice(password_values) for _ in range(number_of_characters)
            )
        )
    return passwords_for_view
