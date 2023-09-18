# Generated by Django 4.2.3 on 2023-09-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestij', '0013_abiturientonlineregister_accountingonlineregister_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherOnlineRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Ad, soyad')),
                ('email', models.EmailField(max_length=256, verbose_name='Email')),
                ('mobile_number', models.CharField(max_length=50, verbose_name='Mobil nömrə')),
                ('identity_card_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Şəxsiyyət vəsiqəsinin nömrəsi')),
                ('speciality', models.TextField(verbose_name='İxtisas')),
                ('section', models.CharField(choices=[('AZ', 'Azərbaycan dili'), ('RU', 'Rus dili')], default='AZ', max_length=2, verbose_name='Bölmə')),
                ('status', models.CharField(choices=[('T', 'Tamamlandı'), ('TM', 'Tamamlanmadı')], default='TM', max_length=2, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Müəllim qeydiyyat',
                'verbose_name_plural': 'Müəllim qeydiyyatlar',
                'ordering': ('-id',),
            },
        ),
    ]