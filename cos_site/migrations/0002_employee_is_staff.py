# Generated by Django 2.2.5 on 2020-01-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
