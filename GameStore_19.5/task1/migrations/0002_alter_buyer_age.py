# Generated by Django 5.1.5 on 2025-02-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
