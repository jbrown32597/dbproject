# Generated by Django 2.1.3 on 2018-11-20 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20181120_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='created_by',
        ),
    ]
