# Generated by Django 4.1.1 on 2022-09-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_taskdata_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
