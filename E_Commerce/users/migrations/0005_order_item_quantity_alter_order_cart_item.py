# Generated by Django 4.2.2 on 2023-07-12 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce_app', '0004_rename_categorie_stuff_category'),
        ('users', '0004_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item_quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commerce_app.stuff'),
        ),
    ]
