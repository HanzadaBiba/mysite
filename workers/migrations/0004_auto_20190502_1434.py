# Generated by Django 2.2 on 2019-05-02 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20190502_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='deps',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workers.Departaments', verbose_name='Подразделение'),
        ),
    ]
