# Generated by Django 4.2.2 on 2023-07-12 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_remove_cart_date_added_cartitem_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('address', models.TextField(max_length=512)),
                ('country', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zip_code', models.PositiveIntegerField()),
                ('cart_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
