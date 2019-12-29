# Generated by Django 3.0 on 2019-12-22 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('date', models.DateField(default=datetime.date.today, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publishing', models.BooleanField(default=True)),
            ],
        ),
    ]