# Generated by Django 4.2.2 on 2023-08-11 06:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0002_creditoffers_loanoffers"),
    ]

    operations = [
        migrations.CreateModel(
            name="invest",
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
                ("occupation", models.CharField(max_length=30)),
                ("time_to_manage", models.BigIntegerField()),
                ("time_to_reach_goal", models.BigIntegerField()),
                (
                    "return_of_investment",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(100.0),
                        ]
                    ),
                ),
                ("location", models.CharField(max_length=15)),
            ],
        ),
    ]
