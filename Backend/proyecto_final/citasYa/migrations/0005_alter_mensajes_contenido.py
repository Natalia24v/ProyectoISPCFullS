# Generated by Django 4.2.1 on 2023-05-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasYa', '0004_alter_locacion_numero_direccion_alter_usuario_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='contenido',
            field=models.CharField(max_length=1000),
        ),
    ]
