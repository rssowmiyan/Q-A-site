# Generated by Django 3.0.5 on 2020-05-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_shadow_banned',
            field=models.BooleanField(default=False),
        ),
    ]