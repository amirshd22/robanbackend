# Generated by Django 3.2.5 on 2021-08-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
