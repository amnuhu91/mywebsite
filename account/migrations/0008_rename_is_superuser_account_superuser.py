# Generated by Django 3.2 on 2021-08-11 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_account_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_superuser',
            new_name='superuser',
        ),
    ]
