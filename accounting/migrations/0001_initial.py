# Generated by Django 4.2.3 on 2023-08-25 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='months', to='service.seasonmodel', verbose_name='Sezon')),
            ],
            options={
                'verbose_name': 'Ay',
                'verbose_name_plural': 'Aylar',
            },
        ),
        migrations.CreateModel(
            name='PaymentInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Ödənişin tarixi')),
                ('payment_amount', models.FloatField(default=0, verbose_name='Ödəniş məbləği')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month_payments', to='accounting.monthmodel', verbose_name='Ay')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_payments', to='service.studentmodel', verbose_name='Tələbə')),
            ],
            options={
                'verbose_name': 'Ödəniş məlumatı',
                'verbose_name_plural': 'Ödəniş məlumatları',
            },
        ),
    ]