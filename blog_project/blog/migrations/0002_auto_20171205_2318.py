# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='catagory_article',
            new_name='catagory',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='user_article',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='article_comment',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_comment',
            new_name='user',
        ),
    ]
