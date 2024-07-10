# Generated by Django 4.2 on 2024-05-02 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0006_remove_chatmessages_to_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessages',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
