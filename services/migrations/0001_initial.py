# Generated by Django 3.2.14 on 2022-11-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'services',
                'managed': False,
            },
        ),
    ]
