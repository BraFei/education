# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_content_file_image_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=course.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=course.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
