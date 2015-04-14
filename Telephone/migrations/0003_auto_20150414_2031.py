# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Telephone.models


class Migration(migrations.Migration):

    dependencies = [
        ('Telephone', '0002_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(verbose_name='Фотография', null=True, blank=True, upload_to=Telephone.models.Employee.upload_name),
        ),
    ]
