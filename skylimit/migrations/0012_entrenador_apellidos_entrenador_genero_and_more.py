# Generated by Django 5.1.1 on 2024-12-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylimit', '0011_alter_grupo_imagen_mensajegrupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='apellidos',
            field=models.CharField(blank=True, max_length=50, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='entrenador',
            name='genero',
            field=models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=10, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='entrenador',
            name='nivel_experiencia',
            field=models.CharField(blank=True, choices=[('Principiante', 'Principiante'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')], max_length=15, verbose_name='Nivel de Experiencia'),
        ),
        migrations.AddField(
            model_name='entrenador',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombre'),
        ),
    ]
