# Generated by Django 3.2 on 2021-08-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='viewable',
            field=models.BooleanField(default=True),
        ),
    ]
