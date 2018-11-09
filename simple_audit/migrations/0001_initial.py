# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('operation', models.PositiveIntegerField(max_length=255, verbose_name='Operation', choices=[(0, 'add'), (1, 'change'), (2, 'delete')])),
                ('object_id', models.UUIDField(db_index=True, default=uuid.UUID('e717764a-0dcf-4134-bb1f-f518dc9be69c'))),
                ('description', models.TextField()),
                ('obj_description', models.CharField(db_index=True, max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'audit',
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.CreateModel(
            name='AuditChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.CharField(max_length=255)),
                ('old_value', models.TextField(null=True, blank=True)),
                ('new_value', models.TextField(null=True, blank=True)),
                ('audit', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='field_changes', to='simple_audit.Audit')),
            ],
            options={
                'db_table': 'audit_change',
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.CreateModel(
            name='AuditRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_id', models.CharField(max_length=255)),
                ('ip', models.IPAddressField()),
                ('path', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('user', models.ForeignKey(on_delete=models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'audit_request',
                'verbose_name': 'Audit',
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.AddField(
            model_name='audit',
            name='audit_request',
            field=models.ForeignKey(on_delete=models.deletion.SET_NULL, to='simple_audit.AuditRequest', null=True),
        ),
        migrations.AddField(
            model_name='audit',
            name='content_type',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
