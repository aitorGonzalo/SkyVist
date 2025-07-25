# Generated by Django 5.1.1 on 2025-01-24 17:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylimit', '0036_metausuario_progresometa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('oro', 'Oro'), ('plata', 'Plata'), ('bronce', 'Bronce')], max_length=10, unique=True)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='logros/')),
            ],
        ),
        migrations.CreateModel(
            name='LogroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_desbloqueo', models.DateTimeField(auto_now_add=True)),
                ('logro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skylimit.logro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logros', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'logro')},
            },
        ),
    ]
