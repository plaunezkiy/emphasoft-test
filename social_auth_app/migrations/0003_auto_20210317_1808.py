# Generated by Django 3.1.7 on 2021-03-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_auth_app', '0002_auto_20210317_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='default/default.png', upload_to='media', verbose_name='Аватар'),
        ),
    ]
