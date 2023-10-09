# Generated by Django 4.2.3 on 2023-10-09 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='language_students', to='service.languagemodel', verbose_name='Xarici dil'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='specialty',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='İxtisas'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, related_name='teacher_students', to='service.teachermodel', verbose_name='Müəllimlər'),
        ),
    ]
