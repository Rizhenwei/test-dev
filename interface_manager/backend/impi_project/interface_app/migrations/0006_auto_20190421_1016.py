# Generated by Django 2.1.7 on 2019-04-21 02:16

from django.db import migrations, models
import django.db.models.deletion
import interface_app.fields.model.object_field
import interface_app.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0005_auto_20190421_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('host', models.CharField(default='', max_length=200, verbose_name='host')),
                ('url', models.CharField(max_length=500, verbose_name='url')),
                ('method', models.CharField(max_length=20, verbose_name='method')),
                ('header', interface_app.fields.model.object_field.ObjectField(default={}, verbose_name='header')),
                ('parameter', interface_app.fields.model.object_field.ObjectField(default={}, verbose_name='parameter')),
                ('parameter_type', models.CharField(default='json', max_length=20, verbose_name='parameter_type, json or form')),
                ('response', interface_app.fields.model.object_field.ObjectField(default='', verbose_name='response')),
                ('response_type', models.CharField(default='json', max_length=20, verbose_name='response_type, json or html')),
                ('assertion', interface_app.fields.model.object_field.ObjectField(default=[], verbose_name='assertion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('interface', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_app.Interface')),
            ],
            bases=(models.Model, interface_app.models.base.Base),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('status', models.IntegerField(choices=[(0, '未执行'), (1, '正在执行'), (2, '执行完成')], default=0, verbose_name='状态')),
            ],
            bases=(models.Model, interface_app.models.base.Base),
        ),
        migrations.CreateModel(
            name='TaskInterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_app.Interface')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_app.Task')),
            ],
            bases=(models.Model, interface_app.models.base.Base),
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=1, verbose_name='version')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_app.Task')),
            ],
            bases=(models.Model, interface_app.models.base.Base),
        ),
        migrations.AddField(
            model_name='interfaceresult',
            name='task_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='interface_app.TaskResult'),
        ),
    ]
