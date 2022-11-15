import logging

from django.core.management import BaseCommand, CommandParser

from apps.contacts_db import models
from apps.contacts_db.services.data_for_output import data_for_db


class Command(BaseCommand):
    help = "Generate amount of contacts for Database"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--amount",
            type=int,
            default=10,
            help="amount of generated contacts",
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        self.logger.info(f"Generate {amount} contacts")

        current_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Current generated amount of contacts: {current_amount}")

        for number, contact in enumerate(data_for_db(amount=amount), start=1):
            self.logger.info(f"Contact generation: {number}/{amount} START")
            contact.save()
            self.logger.info(f"Contacts generated: {number}/{amount} END")

        total_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Total amount of generated contacts: {total_amount}")
