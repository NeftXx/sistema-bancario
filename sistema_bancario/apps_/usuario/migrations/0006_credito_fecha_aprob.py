# Generated by Django 2.1.7 on 2019-04-24 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_remove_notificacion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='fecha_aprob',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
