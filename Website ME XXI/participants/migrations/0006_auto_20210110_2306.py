# Generated by Django 3.1.4 on 2021-01-10 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0005_auto_20201229_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='foto_kartu_pelajar',
            new_name='foto_rapor',
        ),
    ]
