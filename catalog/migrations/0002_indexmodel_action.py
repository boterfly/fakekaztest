# Generated by Django 3.1.2 on 2020-10-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexmodel',
            name='action',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
