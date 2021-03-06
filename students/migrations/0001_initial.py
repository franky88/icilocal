# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrn', models.CharField(max_length=15, unique=True)),
                ('fname', models.CharField(max_length=60, verbose_name='first name')),
                ('lname', models.CharField(max_length=60, verbose_name='last name')),
                ('mname', models.CharField(blank=True, max_length=60, verbose_name='middle name')),
                ('ename', models.CharField(blank=True, max_length=5, verbose_name='extension name')),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='male', max_length=6)),
                ('birth_date', models.DateField(help_text='Date format yyyy-mm-dd, e.g 2000-01-20.')),
                ('age', models.IntegerField(default=15, help_text='Age as of first friday of June.')),
                ('mother_tongue', models.CharField(default='bisaya', max_length=60)),
                ('IP', models.CharField(default='higaonon', help_text='Ethnic group', max_length=60)),
                ('religion', models.CharField(default='roman catholic', max_length=60)),
                ('address', models.TextField(default='--student address--', help_text='Format, house#/Street/Sitio/Purok, Barangay, Municipality/City, Province')),
                ('father_name', models.CharField(default="--father's name of student--", help_text='Format: (Last Name, First Name, Middle Name)', max_length=120)),
                ('mother_name', models.CharField(default="--mother's name of student--", help_text='Format: (Last Name, First Name, Middle Name)', max_length=120)),
                ('guardian_name', models.CharField(blank=True, default='name of student guardian', help_text='Full name of guardian', max_length=160)),
                ('relationship', models.CharField(blank=True, default='--guardian relationship student--', max_length=120)),
                ('contact', models.CharField(blank=True, default='--contact number--', help_text=' contact number of parents or guardian', max_length=13)),
                ('remarks', models.CharField(default='', max_length=60)),
            ],
        ),
    ]
