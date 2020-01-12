# Generated by Django 3.0.2 on 2020-01-08 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0002_kakeibo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakeibo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='kakeibo',
            name='memo',
            field=models.CharField(max_length=500, verbose_name='Memo'),
        ),
    ]
