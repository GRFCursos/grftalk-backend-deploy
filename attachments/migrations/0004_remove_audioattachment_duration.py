# Generated by Django 4.2 on 2024-05-09 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0003_rename_type_fileattachment_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audioattachment',
            name='duration',
        ),
    ]
