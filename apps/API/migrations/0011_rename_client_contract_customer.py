# Generated by Django 4.0.1 on 2022-02-18 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_alter_contract_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='client',
            new_name='customer',
        ),
    ]