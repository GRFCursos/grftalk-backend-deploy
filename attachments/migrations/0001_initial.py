# Generated by Django 4.2 on 2024-04-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('extension', models.CharField(max_length=15)),
                ('size', models.FloatField()),
                ('src', models.TextField()),
                ('type', models.CharField(max_length=45)),
            ],
        ),
    ]
