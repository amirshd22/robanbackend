# Generated by Django 3.1.4 on 2021-06-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210620_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_day_date',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
