# Generated by Django 3.1.4 on 2021-01-10 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='kontak_institusi',
            new_name='kontak_guru_pendamping',
        ),
    ]
