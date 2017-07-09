# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-07-09 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_auto_20170227_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporarydocumenttext',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='temporary_documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='temporarydocumenttext',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='document', to='documents.Document'),
        ),
    ]