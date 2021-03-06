# Generated by Django 3.1.2 on 2021-06-02 19:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.UUIDField(default=uuid.uuid4, help_text='Llave primaria Cliente', primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=25)),
                ('telefono', models.IntegerField(max_length=9)),
                ('email', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=25)),
                ('usuario', models.CharField(max_length=25)),
                ('contrasenia', models.CharField(max_length=8)),
            ],
        ),
    ]
