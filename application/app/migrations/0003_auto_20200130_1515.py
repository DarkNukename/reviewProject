# Generated by Django 3.0.2 on 2020-01-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200130_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdatabase',
            name='uuid',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]