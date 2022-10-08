from apps.data_generator.services import password_generator, login_and_email_generator
from apps.data_generator.models import GenerateUserInfo


def information_for_view(amount: int) -> GenerateUserInfo:
    logins, emails = login_and_email_generator.get_login_and_email(amount=amount)
    passwords = password_generator.passwords(amount=amount)
    for login, email, password in zip(logins, emails, passwords):
        yield GenerateUserInfo(username=login, email=email, password=password)
