# Generated by Django 3.1.2 on 2021-03-31 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitapp', '0006_auto_20210331_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='value',
            new_name='current',
        ),
    ]
