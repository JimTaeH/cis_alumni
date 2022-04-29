# Generated by Django 3.2 on 2022-04-26 11:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0044_auto_20220426_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='success',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achieveTitle', models.CharField(default='#', max_length=50)),
                ('desc', models.TextField(default='#', max_length=2000)),
                ('achieveDate', models.DateField(default=datetime.date.today, max_length=10)),
                ('alumniuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile')),
            ],
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(default='#', max_length=30)),
                ('organizeType', models.CharField(default='#', max_length=10)),
                ('department', models.CharField(default='#', max_length=20)),
                ('jobTitle', models.CharField(default='#', max_length=30)),
                ('jobDesc', models.TextField(default='#', max_length=255)),
                ('alumniuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile')),
            ],
        ),
        migrations.CreateModel(
            name='fieldstudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studyFieldID', models.CharField(default='#', max_length=2)),
                ('studyField', models.CharField(default='#', max_length=50)),
                ('studyMajor', models.CharField(default='#', max_length=30)),
                ('studyMinor', models.CharField(default='#', max_length=30)),
                ('yearStart', models.IntegerField(default=2543)),
                ('yearGraduate', models.IntegerField(default=2547)),
                ('gpa', models.FloatField(default=3.5, max_length=4)),
                ('alumniuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile')),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universityID', models.CharField(default='#', max_length=10)),
                ('degree', models.CharField(default='#', max_length=10)),
                ('university', models.CharField(default='#', max_length=50)),
                ('faculty', models.CharField(default='#', max_length=50)),
                ('major', models.CharField(default='#', max_length=50)),
                ('country', models.CharField(default='#', max_length=20)),
                ('alumniuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile')),
            ],
        ),
    ]
