# Generated by Django 4.2.3 on 2023-09-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_accountant',
            field=models.BooleanField(default=False, verbose_name='Mühasib'),
        ),
    ]
