from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Contacts


def contacts_view(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request,
        "templates_for__contacts_db/content.html",
        {
            "title": "Contacts",
            "contacts_db": contacts,
        },
    )
