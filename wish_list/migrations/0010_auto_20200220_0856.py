# Generated by Django 2.1.5 on 2020-02-20 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0009_auto_20200220_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='checkbox',
            field=models.BooleanField(default=False),
        ),
    ]