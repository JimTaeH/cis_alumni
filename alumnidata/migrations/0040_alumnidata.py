# Generated by Django 3.2 on 2022-04-26 01:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0039_auto_20220426_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumnidata',
            fields=[
                ('alumniID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('phone', models.CharField(default='0123456789', max_length=10)),
                ('dob', models.DateField(default=datetime.date.today, max_length=10)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'lgbtqia2s+')], default='#', max_length=10)),
                ('address', models.TextField(default='#', max_length=2500)),
                ('alumniuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.profile')),
            ],
        ),
    ]
