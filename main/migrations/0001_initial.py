# Generated by Django 4.2.4 on 2023-08-28 06:20

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
                ('place', models.CharField(max_length=255, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('pleasant', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('period', models.PositiveIntegerField(default=1, verbose_name='Периодичность в днях')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вознаграждение')),
                ('time_to_complete', models.PositiveIntegerField(verbose_name='Время на выполнение')),
                ('public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
