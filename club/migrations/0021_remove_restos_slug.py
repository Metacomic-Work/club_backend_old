# Generated by Django 4.1.1 on 2023-06-20 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0020_restos_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="restos",
            name="slug",
        ),
    ]