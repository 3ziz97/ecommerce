# Generated by Django 4.1.5 on 2023-03-07 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0006_cartproduct_delete_brand_cart_total_cartproduct_cart_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproduct',
            old_name='total',
            new_name='subtotal',
        ),
    ]
