# Generated by Django 3.2 on 2022-04-22 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0023_auto_20220422_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='achievement',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='education',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='job',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='studyField',
        ),
        migrations.DeleteModel(
            name='achieve',
        ),
        migrations.DeleteModel(
            name='alumnijob',
        ),
        migrations.DeleteModel(
            name='fieldsofstudy',
        ),
        migrations.DeleteModel(
            name='furthereducation',
        ),
    ]