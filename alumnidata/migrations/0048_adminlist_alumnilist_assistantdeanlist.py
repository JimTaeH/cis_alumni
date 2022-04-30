# Generated by Django 3.2 on 2022-04-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0047_auto_20220429_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldresponible', models.CharField(default='#', max_length=50)),
                ('adminID', models.CharField(default='#', max_length=10)),
                ('firstname', models.CharField(default='#', max_length=50)),
                ('lastname', models.CharField(default='#', max_length=50)),
                ('phone', models.CharField(default='#', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='alumniList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldstudy', models.CharField(default='#', max_length=50)),
                ('yearGraduated', models.IntegerField(default=2543)),
                ('studentID', models.CharField(default='#', max_length=10)),
                ('firstname', models.CharField(default='#', max_length=50)),
                ('lastname', models.CharField(default='#', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='assistantDeanList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistantDeanID', models.CharField(default='#', max_length=10)),
                ('firstname', models.CharField(default='#', max_length=50)),
                ('lastname', models.CharField(default='#', max_length=50)),
                ('phone', models.CharField(default='#', max_length=10)),
            ],
        ),
    ]