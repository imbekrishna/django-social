# Generated by Django 4.2.5 on 2023-09-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_posts', '0004_tag_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
