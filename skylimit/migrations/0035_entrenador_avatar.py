# Generated by Django 5.1.1 on 2025-01-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skylimit', '0034_remove_entrenador_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrenador',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
