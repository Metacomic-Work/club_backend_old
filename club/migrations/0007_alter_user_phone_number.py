# Generated by Django 4.1.1 on 2023-06-16 05:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0006_remove_ratings_photo_url_bookings_product_list_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                max_length=15,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the form of +919999999999.",
                        regex="^\\+?1?\\d{9,14}$",
                    )
                ],
            ),
        ),
    ]
