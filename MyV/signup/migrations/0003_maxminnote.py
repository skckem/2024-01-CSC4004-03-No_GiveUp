# Generated by Django 5.0.4 on 2024-05-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_rename_upload_maxmin_uploadmaxmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaxminNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_note', models.CharField(max_length=5)),
                ('min_note', models.CharField(max_length=5)),
            ],
        ),
    ]
