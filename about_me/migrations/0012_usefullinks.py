# Generated by Django 3.2 on 2021-07-06 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0011_learn'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLinks',
            fields=[
                ('courseparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='about_me.courseparent')),
            ],
            bases=('about_me.courseparent',),
        ),
    ]
