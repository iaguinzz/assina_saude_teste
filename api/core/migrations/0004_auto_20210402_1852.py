# Generated by Django 3.1.5 on 2021-04-02 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210402_1845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Paciente',
        ),
    ]
