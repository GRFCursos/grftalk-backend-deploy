# Generated by Django 4.2 on 2024-04-25 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.TextField(default='/medias/avatars/default-avatar.png'),
        ),
    ]
