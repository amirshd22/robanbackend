# Generated by Django 3.1.4 on 2021-07-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210629_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='character',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
