# Generated by Django 3.2 on 2022-04-22 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0025_auto_20220422_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='alumniname',
            field=models.OneToOneField(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile'),
        ),
    ]