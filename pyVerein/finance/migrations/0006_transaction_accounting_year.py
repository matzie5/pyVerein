# Generated by Django 2.1.1 on 2018-11-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_remove_account_clearing'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='accounting_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
