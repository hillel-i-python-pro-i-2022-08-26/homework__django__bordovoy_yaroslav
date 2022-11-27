import uuid

from django.db import models
from django.urls import reverse


def get_icon_path(instance, filename) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contact/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_icon_path,
    )

    def __str__(self) -> str:
        return f"{self.name} --- {self.phone_number} --- {self.date_of_birth}"

    __repr__ = __str__


    def get_absolute_url(self):
        return reverse(
            "contacts_db:update_contact",
            kwargs={"pk": self.pk},
        )