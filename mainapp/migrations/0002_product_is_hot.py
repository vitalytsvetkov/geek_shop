# Generated by Django 2.2.5 on 2019-09-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='горячий?'),
        ),
    ]
