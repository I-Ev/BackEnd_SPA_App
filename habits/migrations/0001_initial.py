# Generated by Django 4.2.4 on 2023-09-28 05:22

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
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('place', models.CharField(blank=True, max_length=50, null=True, verbose_name='Место')),
                ('time', models.TimeField(auto_now_add=True, null=True, verbose_name='Время')),
                ('action', models.CharField(blank=True, max_length=150, null=True, verbose_name='Действие')),
                ('is_nice', models.BooleanField(blank=True, default=False, null=True, verbose_name='признак приятной привычки')),
                ('periodicity', models.SmallIntegerField(blank=True, null=True, verbose_name='Периодичность в днях')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='Награда')),
                ('duration', models.SmallIntegerField(blank=True, null=True, verbose_name='Продолжительность в секундах')),
                ('is_public', models.BooleanField(blank=True, default=False, null=True, verbose_name='признак публичной привычки')),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ['-created_date'],
            },
        ),
    ]
