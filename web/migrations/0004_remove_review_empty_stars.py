# Generated by Django 4.1.2 on 2022-10-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_review_empty_stars_alter_review_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='empty_stars',
        ),
    ]
