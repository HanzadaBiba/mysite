# Generated by Django 2.2 on 2019-05-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0005_auto_20190502_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament_block',
            name='slug',
            field=models.SlugField(default=1, max_length=255, verbose_name='Слаг'),
            preserve_default=False,
        ),
    ]
