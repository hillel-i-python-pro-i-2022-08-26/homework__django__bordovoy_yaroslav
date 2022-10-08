from faker import Faker
import random


fake = Faker()


def get_login_and_email(amount: int) -> list[str]:
    logins_for_view = []
    for login in range(amount):
        login = f"{fake.first_name()}_{fake.last_name()}_{random.randint(0, 10000)}"
        if login in logins_for_view:
            continue
        logins_for_view.append(login)

    # Получение email
    mail_to_process = []
    for email in range(amount):
        email = fake.domain_name()
        mail_to_process.append(f"@{email}")

    # Обработка логинов для объединения с почтой
    ready_made_names = []
    for login in logins_for_view:
        login = login.split("_")
        ready_made_names.append(f"{login[0]}_{login[1]}")

    # Создаём готовые email
    mail_for_view = [
        name + email for email, name in zip(mail_to_process, ready_made_names)
    ]

    return logins_for_view, mail_for_view

