# Generated by Django 3.1.4 on 2021-01-10 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0003_institution_kontak_sekolah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='kontak_sekolah',
            new_name='kontak_institusi',
        ),
    ]
