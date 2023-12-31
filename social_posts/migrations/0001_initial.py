# Generated by Django 4.2.5 on 2023-09-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('image', models.URLField(max_length=500)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=True, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
