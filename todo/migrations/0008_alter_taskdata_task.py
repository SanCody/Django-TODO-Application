# Generated by Django 4.1.1 on 2022-09-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_taskdata_task_alter_taskdata_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='task',
            field=models.TextField(),
        ),
    ]
