# Generated by Django 5.1.1 on 2024-12-29 18:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylimit', '0009_grupo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupo',
            old_name='fecha_creacion',
            new_name='creado_en',
        ),
        migrations.AddField(
            model_name='grupo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='grupos/'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='miembros',
            field=models.ManyToManyField(blank=True, related_name='grupos_miembros', to=settings.AUTH_USER_MODEL),
        ),
    ]
