# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200, verbose_name='Управление')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('email_outside', models.EmailField(blank=True, max_length=75, null=True, verbose_name='Внешний e-mail')),
                ('email_inside', models.EmailField(blank=True, max_length=75, null=True, verbose_name='Внутренний e-mail')),
            ],
            options={
                'verbose_name': 'Управление',
                'verbose_name_plural': 'Управления',
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=300, verbose_name='Отдел')),
                ('email_outside', models.EmailField(blank=True, max_length=75, null=True, verbose_name='Внешний e-mail')),
                ('email_inside', models.EmailField(blank=True, max_length=75, null=True, verbose_name='Внутренний e-mail')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('department', models.ForeignKey(blank=True, verbose_name='Управление', to='Telephone.Department', null=True)),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('surname', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('work_telephone', models.CharField(help_text='Номера разделяются символом ; - XXXX;YYYY', blank=True, max_length=100, null=True, verbose_name='Служебный телефон')),
                ('private_telephone', models.CharField(help_text='Номера разделяются символом ; - XXXX;YYYY', blank=True, max_length=100, null=True, verbose_name='Мобильный телефон')),
                ('email', models.EmailField(blank=True, max_length=75, null=True, verbose_name='E-mail')),
                ('is_secretary', models.NullBooleanField(verbose_name='Это Приемная', default=False)),
                ('department', models.ForeignKey(blank=True, verbose_name='Управление', to='Telephone.Department', null=True)),
                ('division', models.ForeignKey(blank=True, verbose_name='Отдел', to='Telephone.Division', null=True)),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('po_name', models.CharField(max_length=100, verbose_name='Должность')),
                ('weight', models.PositiveSmallIntegerField(verbose_name='Вес для сортировки', default=1)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ('-weight',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProsecutorsOffice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=300, verbose_name='Прокуратура')),
                ('tel_cod', models.CharField(blank=True, max_length=7, null=True, verbose_name='Телефонный код')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес')),
                ('email_outside', models.EmailField(blank=True, max_length=75, null=True, verbose_name='Внешний e-mail')),
                ('email_inside', models.EmailField(blank=True, max_length=75, null=True, verbose_name='Внутренний e-mail')),
            ],
            options={
                'verbose_name': 'Прокуратура',
                'verbose_name_plural': 'Прокуратуры',
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(verbose_name='Должность', to='Telephone.Position', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='prosecutors_office',
            field=models.ForeignKey(to='Telephone.ProsecutorsOffice', verbose_name='Прокуратура'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='secretary',
            field=models.ForeignKey(blank=True, verbose_name='Выберите приемную', to='Telephone.Employee', null=True),
            preserve_default=True,
        ),
        migrations.AlterOrderWithRespectTo(
            name='employee',
            order_with_respect_to='position',
        ),
        migrations.AddField(
            model_name='division',
            name='prosecutors_office',
            field=models.ForeignKey(blank=True, verbose_name='Прокуратура', to='Telephone.ProsecutorsOffice', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='prosecutors_office',
            field=models.ForeignKey(blank=True, verbose_name='Прокуратура', to='Telephone.ProsecutorsOffice', null=True),
            preserve_default=True,
        ),
    ]
