# Generated by Django 4.0.2 on 2022-05-24 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='image',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
