# Generated by Django 4.0.2 on 2022-05-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientific_name', models.CharField(max_length=100)),
                ('common_name', models.CharField(max_length=100)),
                ('water_use', models.CharField(max_length=50)),
                ('light', models.CharField(max_length=50)),
                ('maintenance', models.CharField(max_length=50)),
            ],
        ),
    ]