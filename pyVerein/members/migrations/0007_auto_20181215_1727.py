# Generated by Django 2.1.1 on 2018-12-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_auto_20181206_1255'),
        ('members', '0006_auto_20181107_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='cost_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='finance.CostCenter'),
        ),
        migrations.AddField(
            model_name='division',
            name='cost_object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='finance.CostObject'),
        ),
        migrations.AddField(
            model_name='division',
            name='debitor_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='finance.Account'),
        ),
        migrations.AddField(
            model_name='division',
            name='income_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='finance.Account'),
        ),
    ]
