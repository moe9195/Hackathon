# Generated by Django 2.1.5 on 2020-02-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0008_bought'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bought',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='checkbox',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.DeleteModel(
            name='Bought',
        ),
    ]
