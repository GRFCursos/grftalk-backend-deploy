# Generated by Django 4.2 on 2024-05-23 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_access',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
