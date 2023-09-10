# Generated by Django 4.2.3 on 2023-09-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_studentmodel_payment_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='payment_amount',
            field=models.FloatField(default=0, verbose_name='Ödəniş məbləği'),
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Ödənişin tarixi'),
        ),
    ]
