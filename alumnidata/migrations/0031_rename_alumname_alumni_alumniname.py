# Generated by Django 3.2 on 2022-04-22 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0030_auto_20220422_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni',
            old_name='alumname',
            new_name='alumniName',
        ),
    ]
