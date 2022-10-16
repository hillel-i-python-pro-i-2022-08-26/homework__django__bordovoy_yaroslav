from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} --- {self.phone_number} --- {self.date_of_birth}"

    __repr__ = __str__
