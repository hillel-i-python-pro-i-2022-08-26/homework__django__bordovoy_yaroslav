import logging

from django.core.management import BaseCommand, CommandParser
from django.utils import timezone

from apps.contacts_db import models


class Command(BaseCommand):
    help = "Delete generated contacts"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Delete all contacts",
        )
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete all contacts",
        )

    def handle(self, *args, **options):

        current_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Current generated amount of contacts: {current_amount}")

        if options["all"]:
            models.Contacts.objects.all().delete()

        required_datetime = timezone.now() - timezone.timedelta(seconds=10)

        if options["delete"]:
            models.Contacts.objects.order_by("created_at").filter(
                created_at__lt=required_datetime
            ).delete()

        total_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Total amount of generated contacts: {total_amount}")
