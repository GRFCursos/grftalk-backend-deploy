# Generated by Django 4.2 on 2024-04-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.TextField(default='/medias/default-avatar.png'),
        ),
    ]
