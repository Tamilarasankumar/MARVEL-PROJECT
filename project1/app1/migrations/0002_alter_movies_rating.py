# Generated by Django 4.1 on 2022-08-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Rating',
            field=models.FloatField(max_length="4"),
        ),
    ]