# Generated by Django 4.2.2 on 2023-07-03 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_userregister_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='username',
        ),
    ]
