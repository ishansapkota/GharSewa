# Generated by Django 4.2.2 on 2023-07-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='customers_pic/'),
        ),
    ]
