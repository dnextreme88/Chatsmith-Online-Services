# Generated by Django 2.2.5 on 2020-01-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos_site', '0002_employee_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='employees/'),
        ),
    ]
