# Generated by Django 4.2.5 on 2023-09-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_posts', '0005_alter_tag_options_tag_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='icons/'),
        ),
    ]