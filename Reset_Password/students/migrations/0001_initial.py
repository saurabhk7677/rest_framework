# Generated by Django 4.1.6 on 2023-02-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First_name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last_name')),
                ('email', models.EmailField(max_length=254)),
                ('classroom', models.CharField(max_length=20, verbose_name='Classroom')),
            ],
        ),
    ]
