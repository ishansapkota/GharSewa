# Generated by Django 4.2.2 on 2023-07-10 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
