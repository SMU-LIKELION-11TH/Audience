# Generated by Django 4.2.2 on 2023-06-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userable',
            name='interest',
            field=models.ManyToManyField(related_name='interests', to='util.interest'),
        ),
    ]
