# Generated by Django 3.2.5 on 2021-08-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userprofile_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
