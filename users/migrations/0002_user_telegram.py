# Generated by Django 4.2.13 on 2024-05-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='телеграм'),
        ),
    ]
