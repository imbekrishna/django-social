# Generated by Django 4.2.5 on 2023-09-08 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_posts', '0008_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='autthor',
            new_name='author',
        ),
    ]