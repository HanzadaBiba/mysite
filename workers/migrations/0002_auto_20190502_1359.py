# Generated by Django 2.2 on 2019-05-02 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departaments',
            name='units',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units_departaments', to='workers.Units', verbose_name='Структура'),
        ),
    ]
