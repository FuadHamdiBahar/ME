# Generated by Django 3.1.4 on 2020-12-28 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_jawaban'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jawaban',
            name='exam_code_participant',
        ),
        migrations.RemoveField(
            model_name='jawaban',
            name='id_participant',
        ),
        migrations.RemoveField(
            model_name='jawaban',
            name='jawaban_benar',
        ),
        migrations.RemoveField(
            model_name='jawaban',
            name='kode_soal',
        ),
        migrations.AddField(
            model_name='jawaban',
            name='id_peserta',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jawaban',
            name='nama_peserta',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jawaban',
            name='jawaban_peserta',
            field=models.CharField(max_length=255),
        ),
    ]
