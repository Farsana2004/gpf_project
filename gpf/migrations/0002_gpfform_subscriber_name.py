# Generated by Django 5.1.1 on 2024-09-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpfform',
            name='subscriber_name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
    ]
