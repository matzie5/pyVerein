# Generated by Django 2.1.5 on 2019-04-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0015_historicalreport_historicalresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreport',
            name='resources',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='resources',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
