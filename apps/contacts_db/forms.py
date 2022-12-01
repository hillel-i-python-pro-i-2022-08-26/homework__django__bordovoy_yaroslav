from django.forms import ModelForm, TextInput

from .models import Contacts


class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ["name", "phone_number", "date_of_birth", "avatar"]

        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter name",
                }
            ),
            "phone_number": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),
            "date_of_birth": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter date of birth (year-month-date)",
                }
            ),
        }
