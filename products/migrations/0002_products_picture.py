# Generated by Django 4.1.2 on 2022-10-13 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.URLField(default='https://www.freepnglogos.com/uploads/mobile-png/samsung-mobile-png-14.png'),
        ),
    ]