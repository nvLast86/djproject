# Generated by Django 4.2.7 on 2024-01-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='признак текущей версии'),
        ),
    ]
