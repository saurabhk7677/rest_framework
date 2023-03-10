# Generated by Django 4.1.6 on 2023-02-06 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mi', models.CharField(max_length=50)),
                ('first', models.CharField(max_length=70)),
                ('last', models.CharField(max_length=70)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('address3', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField()),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField()),
                ('phone', models.PositiveIntegerField()),
                ('dail_code', models.PositiveIntegerField()),
                ('alt_phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('show', models.CharField(max_length=100)),
                ('vender_id', models.PositiveIntegerField()),
                ('rank', models.IntegerField()),
                ('owner', models.CharField(max_length=70)),
                ('comments', models.TextField(max_length=300)),
            ],
        ),
    ]
