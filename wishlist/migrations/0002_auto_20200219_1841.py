# Generated by Django 2.1.5 on 2020-02-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='static/noimage.jpg', upload_to=''),
        ),
    ]