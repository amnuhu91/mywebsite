# Generated by Django 3.2 on 2022-07-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0017_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcontact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]
