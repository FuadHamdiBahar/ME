# Generated by Django 3.1.4 on 2021-01-02 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0017_jawabanfast'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fastsoal',
            old_name='soal',
            new_name='foto_soal',
        ),
    ]
