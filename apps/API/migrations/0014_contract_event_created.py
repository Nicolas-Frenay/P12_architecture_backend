# Generated by Django 4.0.1 on 2022-03-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0013_event_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='event_created',
            field=models.BooleanField(default=False),
        ),
    ]
