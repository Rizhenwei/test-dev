# Generated by Django 2.1.7 on 2019-05-12 03:33

from django.db import migrations, models
import interface_app.fields.model.object_field
import interface_app.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0007_interfaceresult_success'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('method', models.CharField(default='get', max_length=20, verbose_name='method')),
                ('response', interface_app.fields.model.object_field.ObjectField(default={}, verbose_name='response')),
            ],
            bases=(models.Model, interface_app.models.base.Base),
        ),
    ]
