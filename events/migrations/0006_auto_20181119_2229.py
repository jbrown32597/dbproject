# Generated by Django 2.1.3 on 2018-11-20 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20181119_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rso',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
