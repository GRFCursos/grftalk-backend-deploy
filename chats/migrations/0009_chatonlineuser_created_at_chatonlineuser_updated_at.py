# Generated by Django 4.2 on 2024-05-23 04:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0008_rename_chatmessages_chatmessage_chatonlineuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatonlineuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatonlineuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
