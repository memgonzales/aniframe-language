# Generated by Django 4.0 on 2023-11-10 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_rename_content_notes_code_notes_filename"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Notes",
            new_name="Codes",
        ),
    ]