# Generated by Django 4.0.1 on 2022-03-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_remove_event_event_status_event_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_status',
            field=models.BooleanField(default=True),
        ),
    ]
