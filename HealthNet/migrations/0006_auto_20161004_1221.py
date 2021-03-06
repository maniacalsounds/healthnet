# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealthNet', '0005_auto_20161002_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='cur_hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admitted', to='HealthNet.Hospital'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HealthNet.Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='preferred_hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preferred', to='HealthNet.Hospital'),
        ),
    ]
