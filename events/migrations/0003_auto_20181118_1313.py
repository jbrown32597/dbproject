# Generated by Django 2.1.3 on 2018-11-18 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181118_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='events.University'),
        ),
    ]