from django.contrib import admin

from . import models


@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "date_of_birth")
    search_fields = ("name", "phone_number", "date_of_birth")
    date_hierarchy = "date_of_birth"
    ordering = ("-modified_at", "-created_at")
    list_per_page = 20
    search_help_text = "Enter name, phone number or date of birth"

