# Generated by Django 2.2.5 on 2019-09-19 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketslot',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время изменения'),
        ),
        migrations.AlterField(
            model_name='basketslot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]