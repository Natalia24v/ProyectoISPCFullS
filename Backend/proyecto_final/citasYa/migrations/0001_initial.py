# Generated by Django 4.2.1 on 2023-05-19 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField(verbose_name=30)),
                ('genero', models.CharField(max_length=30)),
                ('interes', models.CharField(max_length=100)),
                ('bio_personal', models.TextField(max_length=1000)),
                ('limite_distancia', models.IntegerField(verbose_name=10)),
                ('rango_edad', models.IntegerField(verbose_name=3)),
            ],
            options={
                'verbose_name': 'Datos de usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='unmatch',
            fields=[
                ('id_usuario_bloqueado', models.AutoField(primary_key=True, serialize=False)),
                ('causa', models.CharField(max_length=1000)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasYa.usuario')),
            ],
            options={
                'verbose_name': 'Lista de contactos rechazados',
                'verbose_name_plural': 'unmatches',
                'db_table': 'unmatch',
            },
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id_premiun', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_plan', models.CharField(max_length=100)),
                ('metodo_pago', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasYa.usuario')),
            ],
            options={
                'verbose_name': 'Usuarios premiun',
                'verbose_name_plural': 'planes',
                'db_table': 'planes',
            },
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('contenido', models.CharField(max_length=10)),
                ('id_usuario2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasYa.usuario')),
            ],
            options={
                'verbose_name': 'chats de usuarios',
                'verbose_name_plural': 'mensajes',
                'db_table': 'mensaje',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id_match', models.AutoField(primary_key=True, serialize=False)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasYa.usuario')),
            ],
            options={
                'verbose_name': 'Usuario que hicieron match',
                'verbose_name_plural': 'Matchs',
                'db_table': 'Match',
            },
        ),
        migrations.CreateModel(
            name='Locacion',
            fields=[
                ('id_locacion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_calle', models.CharField(max_length=100)),
                ('numero_direccion', models.IntegerField(verbose_name=10)),
                ('barrio', models.CharField(max_length=10)),
                ('provincia', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=10)),
                ('pais', models.CharField(max_length=10)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasYa.usuario')),
            ],
            options={
                'verbose_name': 'locacion de usuario',
                'verbose_name_plural': 'locaciones',
                'db_table': 'locacion',
            },
        ),
        migrations.CreateModel(
            name='Likeados',
            fields=[
                ('id_like', models.AutoField(primary_key=True, serialize=False)),
                ('lista_likes', models.CharField(max_length=1000)),
                ('lista_dilikes', models.CharField(max_length=1000)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citasYa.usuario')),
            ],
            options={
                'verbose_name': 'Usuario likeados y dislikeados',
                'verbose_name_plural': 'likeados',
                'db_table': 'likeado',
            },
        ),
    ]
