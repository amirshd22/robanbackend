# Generated by Django 3.2.5 on 2021-08-14 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_delete_mirror'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('username', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('faceRecognition_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('character', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('lastName', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('birth_day_date', models.CharField(max_length=500, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('interests', models.ManyToManyField(blank=True, related_name='topic_members_interests', to='users.TopicTag')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
