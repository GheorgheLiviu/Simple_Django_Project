# Generated by Django 4.2.4 on 2023-08-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0002_student_trainer"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="profile",
            field=models.ImageField(null=True, upload_to="profiles_student/"),
        ),
    ]