# Generated by Django 4.0 on 2023-11-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notes",
            name="title",
        ),
        migrations.AlterField(
            model_name="notes",
            name="content",
            field=models.TextField(),
        ),
    ]
