# Generated by Django 4.2.3 on 2023-07-06 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_userable_reply_userable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='postable',
        ),
    ]