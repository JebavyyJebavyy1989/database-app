# Generated by Django 3.0.7 on 2020-06-04 11:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("indigo", "0002_indigo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("public_id", models.CharField(max_length=200, unique=True)),
                ("exists", models.BooleanField(default=False)),
                ("status_public", models.BooleanField(default=False)),
                (
                    "data_public",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
                (
                    "data_private",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
