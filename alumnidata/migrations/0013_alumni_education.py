# Generated by Django 3.2 on 2022-04-22 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0012_alumni_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='education',
            field=models.ForeignKey(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.furthereducation'),
        ),
    ]