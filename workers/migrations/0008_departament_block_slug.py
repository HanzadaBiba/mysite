# Generated by Django 2.2 on 2019-05-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0007_remove_departament_block_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament_block',
            name='slug',
            field=models.SlugField(default=1, max_length=255, verbose_name='Слаг'),
            preserve_default=False,
        ),
    ]