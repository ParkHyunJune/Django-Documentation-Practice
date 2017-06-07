# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0003_student_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('-name',)},
        ),
        migrations.AddField(
            model_name='student',
            name='cars',
            field=models.ManyToManyField(related_name='introduction_to_models_students', related_query_name='introduction_to_models_student', to='introduction_to_models.Car'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='cars',
            field=models.ManyToManyField(related_name='introduction_to_models_teachers', related_query_name='introduction_to_models_teacher', to='introduction_to_models.Car'),
        ),
    ]