# Generated by Django 3.1.4 on 2021-06-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210620_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='topic_interests', to='users.TopicTag'),
        ),
    ]
