# Generated by Django 4.1.1 on 2023-06-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_remove_taskdata_title_taskdata_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='desc',
            field=models.TextField(max_length=300),
        ),
    ]