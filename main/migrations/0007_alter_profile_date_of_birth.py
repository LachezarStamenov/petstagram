# Generated by Django 4.1.1 on 2022-09-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_petphoto_photo_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
