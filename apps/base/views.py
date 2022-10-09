from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.base.services.random_name_generation import generate_random_name


def greeting_for_user(
    request: HttpRequest, username: str | None = None
) -> HttpResponse:
    if username is None:
        username = generate_random_name()

    return render(
        request,
        "base.html",
        {"homepage": f"Hello, {username}! Welcome to Django homework!"},
    )
