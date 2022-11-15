from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactsForm
from .models import Contacts


def show_all(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request,
        "templates_for__contacts_db/base_content.html",
        {
            "title": "Contacts",
            "contacts": contacts,
        },
    )


def contact(request: HttpRequest, pk: Contacts.pk) -> HttpResponse:
    contact = get_object_or_404(Contacts, pk=pk)
    return render(
        request,
        "templates_for__contacts_db/contact.html",
        {
            "title": "Contact information",
            "contact": contact,
        },
    )


def search_contact(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "templates_for__contacts_db/search_contact.html",
        {
            "title": "Search contact",
        },
    )


def create_contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect("contacts_db:contact", pk=contact.pk)
    else:
        form = ContactsForm()
    return render(
        request,
        "templates_for__contacts_db/create_contact.html",
        {
            "title": "Create contact",
            "form": form,
        },
    )


def read_contact(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")

    if query.startswith("0"):
        contact = Contacts.objects.get(phone=query)
    else:
        contact = Contacts.objects.get(pk=query)
    return render(
        request,
        "templates_for__contacts_db/read_contact.html",
        {
            "title": "Contact information",
            "contact": contact,
        },
    )


def update_contact(request: HttpRequest, pk: Contacts.pk) -> HttpResponse:
    contact = get_object_or_404(Contacts, pk=pk)
    if request.method == "POST":
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts_db:contact", pk=pk)
        else:
            form = ContactsForm(instance=contact)
    return render(
        request,
        "templates_for__contacts_db/update_contact.html",
        {
            "title": "Update contact",
            "form": form,
        },
    )


def delete_contact(request: HttpRequest, pk: Contacts.pk) -> HttpResponse:
    contact = get_object_or_404(Contacts, pk=pk)
    contact.delete()
    return redirect("contacts_db:index")
