# Generated by Django 5.0.4 on 2024-05-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_MAXMIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_file', models.FileField(upload_to='userVoice/')),
                ('min_file', models.FileField(upload_to='userVoice/')),
            ],
        ),
    ]