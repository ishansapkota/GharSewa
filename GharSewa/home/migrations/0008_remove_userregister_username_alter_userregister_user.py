# Generated by Django 4.2.2 on 2023-07-03 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_userregister_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='username',
        ),
        migrations.AlterField(
            model_name='userregister',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
