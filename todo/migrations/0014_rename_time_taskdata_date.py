# Generated by Django 4.1.1 on 2023-06-08 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_alter_taskdata_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskdata',
            old_name='time',
            new_name='date',
        ),
    ]
