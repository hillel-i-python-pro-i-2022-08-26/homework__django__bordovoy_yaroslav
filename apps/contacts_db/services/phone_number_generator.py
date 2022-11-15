import random
import secrets
from string import digits


def get_phone() -> str:
    operator_code = [
        "050",
        "063",
        "067",
        "068",
        "073",
        "096",
        "097",
        "095",
        "098",
        "099",
    ]
    subscriber_number = "".join(secrets.choice(digits) for _ in range(7))

    return f"+38{random.choice(operator_code)}{subscriber_number}"
