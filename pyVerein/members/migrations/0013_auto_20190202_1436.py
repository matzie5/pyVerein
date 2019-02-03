# Generated by Django 2.1.5 on 2019-02-02 13:36

from django.db import migrations, models
import django.db.models.deletion
import members.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_auto_20190131_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=members.models.get_file_path)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='member',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='file',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
    ]