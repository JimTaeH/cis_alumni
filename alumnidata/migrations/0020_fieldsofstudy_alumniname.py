# Generated by Django 3.2 on 2022-04-22 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0019_auto_20220422_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldsofstudy',
            name='alumniName',
            field=models.OneToOneField(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile'),
        ),
    ]
