from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Contacts


class ContactsListView(ListView):
    model = Contacts
    template_name = "templates_for__contacts_db/contacts_list.html"


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


"""
class ContactsView(TemplateView):
    template_name = "templates_for__contacts_db/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = Contacts.objects.get(pk=context["pk"])
        context['contact'] = contact
        context['title'] = f"Info {contact.name}."
        return context
"""


def search_contact(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "templates_for__contacts_db/search_contact.html",
        {
            "title": "Search contact",
        },
    )


class ContactsCreateView(CreateView):
    model = Contacts
    fields = (
        "name",
        "phone_number",
        "date_of_birth",
        "avatar",
    )
    template_name = "templates_for__contacts_db/create_contact.html"

    def get_success_url(self):
        return reverse_lazy("contacts_db:contact", kwargs={"pk": self.object.pk})


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


class ContactsUpdateView(UpdateView):
    model = Contacts
    fields = (
        "name",
        "phone_number",
        "date_of_birth",
        "avatar",
    )
    template_name = "templates_for__contacts_db/contact_update_form.html"

    def get_success_url(self):
        return reverse_lazy("contacts_db:contact", kwargs={"pk": self.object.pk})


class ContactsDeleteView(DeleteView):
    model = Contacts
    success_url = reverse_lazy("contacts_db:index")


"""
    
"""
