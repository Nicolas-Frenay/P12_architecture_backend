# Generated by Django 4.0.1 on 2022-02-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_updated',
            field=models.DateTimeField(default=models.DateTimeField()),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]