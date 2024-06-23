# Generated by Django 4.2.4 on 2023-08-09 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("trainer", "0001_initial"),
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="trainer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trainer.trainer",
            ),
        ),
    ]
