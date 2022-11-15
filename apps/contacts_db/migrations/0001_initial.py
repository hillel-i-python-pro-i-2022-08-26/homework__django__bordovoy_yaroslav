# Generated by Django 4.1.1 on 2022-10-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.PositiveBigIntegerField()),
                ("date_of_birth", models.PositiveSmallIntegerField()),
            ],
        ),
    ]
