# Generated by Django 2.1.5 on 2019-03-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_detalle_cupomax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='cupoMax',
            field=models.IntegerField(),
        ),
    ]