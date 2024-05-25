# Generated by Django 4.2.13 on 2024-05-21 18:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='действие')),
                ('is_nice', models.BooleanField(default=True, verbose_name='признак приятной привычки')),
                ('periodicity', models.CharField(choices=[('1', 'ежедневно'), ('2', 'каждые два дня'), ('3', 'каждые три дня'), ('4', 'каждые четыре дня'), ('5', 'каждые пять дня'), ('6', 'каждые шесть дня'), ('7', 'еженедельно')], default='1', max_length=1, verbose_name='переодичность')),
                ('reward', models.CharField(blank=True, default='съесть яблоко', max_length=100, null=True, verbose_name=' вознаграждение')),
                ('time_complete', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='признак публичности')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('pk',),
            },
        ),
    ]