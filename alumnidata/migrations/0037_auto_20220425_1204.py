# Generated by Django 3.2 on 2022-04-25 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnidata', '0036_alumnidata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnidata',
            name='achieve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.success'),
        ),
        migrations.AlterField(
            model_name='alumnidata',
            name='educations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.education'),
        ),
        migrations.AlterField(
            model_name='alumnidata',
            name='jobs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.job'),
        ),
        migrations.AlterField(
            model_name='alumnidata',
            name='studyin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnidata.fieldstudy'),
        ),
    ]