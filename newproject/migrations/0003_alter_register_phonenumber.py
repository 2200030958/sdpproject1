# Generated by Django 3.2.15 on 2024-02-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newproject', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phonenumber',
            field=models.PositiveBigIntegerField(),
        ),
    ]
