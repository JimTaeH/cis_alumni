# Generated by Django 3.2 on 2022-04-22 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0007_auto_20220422_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='achieve',
            field=models.ForeignKey(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.achievement'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='faculty',
            field=models.ForeignKey(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.alumnifaculty'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='furtherEdu',
            field=models.ForeignKey(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.furthereducation'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='job',
            field=models.ForeignKey(default='#', on_delete=django.db.models.deletion.CASCADE, to='alumnidata.alumnijob'),
        ),
    ]
