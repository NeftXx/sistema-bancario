# Generated by Django 2.1.7 on 2019-04-01 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cod_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=30, unique=True)),
                ('nick_name', models.CharField(max_length=12, unique=True)),
                ('correo', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Rol')),
            ],
        ),
    ]