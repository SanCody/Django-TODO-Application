# Generated by Django 4.1.1 on 2022-09-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('task', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Todo',
            },
        ),
    ]