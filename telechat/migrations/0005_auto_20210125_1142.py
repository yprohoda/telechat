# Generated by Django 3.1.5 on 2021-01-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telechat', '0004_auto_20210123_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_id',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='chat',
            name='manager_id',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='chat',
            name='user_id',
            field=models.TextField(default=0),
        ),
    ]