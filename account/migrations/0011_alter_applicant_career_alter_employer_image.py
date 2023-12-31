# Generated by Django 4.2.2 on 2023-07-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_applicant_age_alter_employer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='career',
            field=models.ImageField(blank=True, null=True, upload_to='applicant_career/'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company_profile/'),
        ),
    ]
