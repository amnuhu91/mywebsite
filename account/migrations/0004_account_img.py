# Generated by Django 3.2 on 2021-07-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210703_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='img',
            field=models.ImageField(default='cancer.jpg', upload_to=''),
        ),
    ]
