# Generated by Django 4.1.5 on 2023-04-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_category_remove_order_product_remove_order_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="static"),
        ),
    ]