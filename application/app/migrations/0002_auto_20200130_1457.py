# Generated by Django 3.0.2 on 2020-01-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdatabase',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
