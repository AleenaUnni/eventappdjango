# Generated by Django 4.2.5 on 2023-09-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='aleena'),
            preserve_default=False,
        ),
    ]
