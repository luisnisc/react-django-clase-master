# Generated by Django 4.2.1 on 2023-10-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_fecha_examen_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]