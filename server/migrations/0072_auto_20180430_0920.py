# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0071_remove_updatehistory_pending_recorded'),
    ]

    Machine = apps.get_model("server", "Machine")
    machines_to_clean = Machine.objects.filter(activity__gt='',activity__isnull=False)
    for machine_to_clean in machines_to_clean:
        machine_to_clean.activity = ''
        machine_to_clean.save()

    operations = [
        migrations.RunPython(clean_model_names),
        migrations.AlterField(
            model_name='machine',
            name='activity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='machine',
            name='report_format',
            field=models.CharField(choices=[(b'base64', b'base64'), (b'base64bz2', b'base64bz2'), (b'bz2', b'bz2')], default=b'base64bz2', editable=False, max_length=256),
        ),
    ]
