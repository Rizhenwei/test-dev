# Generated by Django 2.1.7 on 2019-05-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0006_auto_20190421_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='interfaceresult',
            name='success',
            field=models.BooleanField(default=False, verbose_name='测试结果'),
        ),
    ]