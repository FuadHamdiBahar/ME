# Generated by Django 3.1.4 on 2020-12-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0003_auto_20201229_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], max_length=30),
        ),
    ]
