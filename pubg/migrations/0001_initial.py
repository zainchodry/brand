# Generated by Django 5.1.2 on 2024-10-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pubg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_place', models.CharField(max_length=50)),
                ('about_school', models.TextField()),
            ],
        ),
    ]
