# Generated by Django 3.1.4 on 2020-12-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_soal_tingkat'),
    ]

    operations = [
        migrations.AddField(
            model_name='jawaban',
            name='tingkat',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
