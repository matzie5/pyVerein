# Generated by Django 2.1.1 on 2018-09-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180727_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='user'),
        ),
    ]