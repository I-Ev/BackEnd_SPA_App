# Generated by Django 4.2.4 on 2023-09-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_phone_user_chat_id_user_telegram_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='update_id',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='ID последнего сообщения'),
        ),
    ]