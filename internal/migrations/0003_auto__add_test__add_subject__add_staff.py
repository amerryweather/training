# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Test'
        db.create_table(u'internal_test', (
            ('test_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Staff'])),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['internal.Subject'])),
            ('test_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('mark', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'internal', ['Test'])

        # Adding model 'Subject'
        db.create_table(u'internal_subject', (
            ('subject_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('subject_title', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('marks', self.gf('django.db.models.fields.IntegerField')()),
            ('pass_mark', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'internal', ['Subject'])

        # Adding model 'Staff'
        db.create_table(u'internal_staff', (
            ('staff_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'internal', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Test'
        db.delete_table(u'internal_test')

        # Deleting model 'Subject'
        db.delete_table(u'internal_subject')

        # Deleting model 'Staff'
        db.delete_table(u'internal_staff')


    models = {
        u'internal.staff': {
            'Meta': {'object_name': 'Staff'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'staff_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'internal.subject': {
            'Meta': {'object_name': 'Subject'},
            'marks': ('django.db.models.fields.IntegerField', [], {}),
            'pass_mark': ('django.db.models.fields.IntegerField', [], {}),
            'subject_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'subject_title': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'internal.test': {
            'Meta': {'object_name': 'Test'},
            'mark': ('django.db.models.fields.IntegerField', [], {}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['internal.Staff']"}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['internal.Subject']"}),
            'test_date': ('django.db.models.fields.DateTimeField', [], {}),
            'test_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['internal']