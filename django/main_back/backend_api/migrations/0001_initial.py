# Generated by Django 5.1.2 on 2024-10-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
