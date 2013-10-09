# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Machine.memory'
        db.alter_column(u'server_machine', 'memory', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Machine.hd_space'
        db.alter_column(u'server_machine', 'hd_space', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Machine.munki_version'
        db.alter_column(u'server_machine', 'munki_version', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Machine.console_user'
        db.alter_column(u'server_machine', 'console_user', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Machine.machine_model'
        db.alter_column(u'server_machine', 'machine_model', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Machine.cpu_type'
        db.alter_column(u'server_machine', 'cpu_type', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Machine.cpu_speed'
        db.alter_column(u'server_machine', 'cpu_speed', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

    def backwards(self, orm):

        # Changing field 'Machine.memory'
        db.alter_column(u'server_machine', 'memory', self.gf('django.db.models.fields.CharField')(default='1 GB', max_length=256))

        # User chose to not deal with backwards NULL issues for 'Machine.hd_space'
        raise RuntimeError("Cannot reverse this migration. 'Machine.hd_space' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Machine.hd_space'
        db.alter_column(u'server_machine', 'hd_space', self.gf('django.db.models.fields.CharField')(max_length=256))

        # User chose to not deal with backwards NULL issues for 'Machine.munki_version'
        raise RuntimeError("Cannot reverse this migration. 'Machine.munki_version' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Machine.munki_version'
        db.alter_column(u'server_machine', 'munki_version', self.gf('django.db.models.fields.CharField')(max_length=256))

        # User chose to not deal with backwards NULL issues for 'Machine.console_user'
        raise RuntimeError("Cannot reverse this migration. 'Machine.console_user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Machine.console_user'
        db.alter_column(u'server_machine', 'console_user', self.gf('django.db.models.fields.CharField')(max_length=256))

        # User chose to not deal with backwards NULL issues for 'Machine.machine_model'
        raise RuntimeError("Cannot reverse this migration. 'Machine.machine_model' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Machine.machine_model'
        db.alter_column(u'server_machine', 'machine_model', self.gf('django.db.models.fields.CharField')(max_length=256))

        # User chose to not deal with backwards NULL issues for 'Machine.cpu_type'
        raise RuntimeError("Cannot reverse this migration. 'Machine.cpu_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Machine.cpu_type'
        db.alter_column(u'server_machine', 'cpu_type', self.gf('django.db.models.fields.CharField')(max_length=256))

        # User chose to not deal with backwards NULL issues for 'Machine.cpu_speed'
        raise RuntimeError("Cannot reverse this migration. 'Machine.cpu_speed' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Machine.cpu_speed'
        db.alter_column(u'server_machine', 'cpu_speed', self.gf('django.db.models.fields.CharField')(max_length=256))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'server.businessunit': {
            'Meta': {'ordering': "['name']", 'object_name': 'BusinessUnit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        u'server.fact': {
            'Meta': {'ordering': "['fact_name']", 'object_name': 'Fact'},
            'fact_data': ('django.db.models.fields.TextField', [], {}),
            'fact_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.Machine']"})
        },
        u'server.machine': {
            'Meta': {'ordering': "['hostname']", 'object_name': 'Machine'},
            'activity': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'console_user': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'cpu_speed': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'cpu_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'errors': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hd_space': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'machine_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.MachineGroup']"}),
            'machine_model': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'manifest': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'memory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'munki_version': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'report': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'warnings': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'server.machinegroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'MachineGroup'},
            'business_unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['server.BusinessUnit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manifest': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'server.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'SO'", 'max_length': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['server']