# Generated by Django 3.0.5 on 2020-04-18 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_question_answers_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
