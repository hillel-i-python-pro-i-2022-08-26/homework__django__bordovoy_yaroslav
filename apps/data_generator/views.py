from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.data_generator.services.data_for_output import information_for_view


def users_data_view(request: HttpRequest, amount: int | None = None) -> HttpResponse:
    if amount is None:
        amount = 10
    return render(
        request,
        "templates_for__data_generator/content.html",
        {"title": "User data", "user_info": information_for_view(amount=amount)},
    )
