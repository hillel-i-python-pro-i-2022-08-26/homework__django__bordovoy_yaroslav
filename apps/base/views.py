from django.http import HttpRequest, HttpResponse

from apps.base.services.random_name_generation import generate_random_name


def greeting_for_user(request: HttpRequest, username: str = None) -> HttpResponse:
    if username is None:
        username = generate_random_name()

    return HttpResponse(f"<h2>Hello, {username}. Welcome to Django homework!</h2>")
