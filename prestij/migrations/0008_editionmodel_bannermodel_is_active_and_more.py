# Generated by Django 4.2.3 on 2023-08-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestij', '0007_alter_settingsmodel_about_page_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048, verbose_name='Başlıq')),
                ('image', models.ImageField(blank=True, null=True, upload_to='edition_images/', verbose_name='Şəkil')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Məzmun')),
                ('is_active', models.BooleanField(default=False, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Nəşr',
                'verbose_name_plural': 'Nəşrlərimiz',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='branchcontactnumbermodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='branchmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='contactinformationmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='photogalleryitem',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='photogallerymodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='servicemodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='about_active',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='favicon_active',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='logo_active',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='socialmediamodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='successitemmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='success_images/', verbose_name='Şəkil'),
        ),
        migrations.AddField(
            model_name='successitemmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='successitemmodel',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Ad soyad'),
        ),
        migrations.AddField(
            model_name='successmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='teachermodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='videogallerymodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='about_page_active',
            field=models.BooleanField(default=True, verbose_name='Haqqımızda'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='contact_page_active',
            field=models.BooleanField(default=True, verbose_name='Əlaqə'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='edition_page_active',
            field=models.BooleanField(default=True, verbose_name='Nəşrlərimiz'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='gallery_page_active',
            field=models.BooleanField(default=True, verbose_name='Qalereya'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='register_page_active',
            field=models.BooleanField(default=True, verbose_name='Kursa onlayn qeydiyyat'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='resume_page_active',
            field=models.BooleanField(default=True, verbose_name='CV göndər'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='service_page_active',
            field=models.BooleanField(default=True, verbose_name='Xidmətlərimiz'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='success_page_active',
            field=models.BooleanField(default=True, verbose_name='Uğurlarımız'),
        ),
    ]
