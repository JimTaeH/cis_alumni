# Generated by Django 3.2 on 2022-04-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default='#', max_length=15),
        ),
    ]
