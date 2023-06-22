# Generated by Django 4.1.1 on 2023-06-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0023_notification"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="status",
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="notification",
            name="message",
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]