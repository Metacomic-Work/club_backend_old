# Generated by Django 4.1.1 on 2023-06-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("club", "0013_bookings_product_list_alter_bookings_booking_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookings",
            name="booking_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]