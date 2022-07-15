# Generated by Django 4.0.4 on 2022-07-15 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='body',
            field=models.TextField(default='message..'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friend',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='chatapp.profile'),
        ),
    ]