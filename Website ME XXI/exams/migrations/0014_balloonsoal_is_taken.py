# Generated by Django 3.1.4 on 2020-12-29 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0013_jawaban_tingkat'),
    ]

    operations = [
        migrations.AddField(
            model_name='balloonsoal',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
