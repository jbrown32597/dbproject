# Generated by Django 2.1.3 on 2018-11-20 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20181119_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='rso',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]