# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AnswerOffered'
        db.create_table(u'answer_offered', (
            ('answer_offered_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('answer_text', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'feedback', ['AnswerOffered'])

        # Adding model 'Form'
        db.create_table(u'form', (
            ('form_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attendee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Attendee'])),
            ('training_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.TrainingType'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'feedback', ['Form'])

        # Adding model 'Attendee'
        db.create_table(u'attendee', (
            ('attendee_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Company'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedback.Role'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('experience', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'feedback', ['Attendee'])


    def backwards(self, orm):
        # Deleting model 'AnswerOffered'
        db.delete_table(u'answer_offered')

        # Deleting model 'Form'
        db.delete_table(u'form')

        # Deleting model 'Attendee'
        db.delete_table(u'attendee')


    models = {
        u'feedback.answer': {
            'Meta': {'object_name': 'Answer', 'db_table': "u'answer'", 'managed': 'False'},
            'answer_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'answer_offered': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AnswerOffered']"}),
            'answer_text': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Form']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Question']"})
        },
        u'feedback.answeroffered': {
            'Meta': {'object_name': 'AnswerOffered', 'db_table': "u'answer_offered'"},
            'answer_offered_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'answer_text': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        u'feedback.attendee': {
            'Meta': {'object_name': 'Attendee', 'db_table': "u'attendee'"},
            'attendee_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Company']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Role']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'feedback.authgroup': {
            'Meta': {'object_name': 'AuthGroup', 'db_table': "u'auth_group'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'feedback.authgrouppermissions': {
            'Meta': {'object_name': 'AuthGroupPermissions', 'db_table': "u'auth_group_permissions'", 'managed': 'False'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthPermission']"})
        },
        u'feedback.authpermission': {
            'Meta': {'object_name': 'AuthPermission', 'db_table': "u'auth_permission'", 'managed': 'False'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.DjangoContentType']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'feedback.authuser': {
            'Meta': {'object_name': 'AuthUser', 'db_table': "u'auth_user'", 'managed': 'False'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {}),
            'is_staff': ('django.db.models.fields.IntegerField', [], {}),
            'is_superuser': ('django.db.models.fields.IntegerField', [], {}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'feedback.authusergroups': {
            'Meta': {'object_name': 'AuthUserGroups', 'db_table': "u'auth_user_groups'", 'managed': 'False'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthUser']"})
        },
        u'feedback.authuseruserpermissions': {
            'Meta': {'object_name': 'AuthUserUserPermissions', 'db_table': "u'auth_user_user_permissions'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthPermission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthUser']"})
        },
        u'feedback.company': {
            'Meta': {'object_name': 'Company', 'db_table': "u'company'", 'managed': 'False'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'company_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'town_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'feedback.djangoadminlog': {
            'Meta': {'object_name': 'DjangoAdminLog', 'db_table': "u'django_admin_log'", 'managed': 'False'},
            'action_flag': ('django.db.models.fields.IntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {}),
            'change_message': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.DjangoContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.AuthUser']"})
        },
        u'feedback.djangocontenttype': {
            'Meta': {'object_name': 'DjangoContentType', 'db_table': "u'django_content_type'", 'managed': 'False'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feedback.djangosession': {
            'Meta': {'object_name': 'DjangoSession', 'db_table': "u'django_session'", 'managed': 'False'},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        },
        u'feedback.form': {
            'Meta': {'object_name': 'Form', 'db_table': "u'form'"},
            'attendee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.Attendee']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'form_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'training_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedback.TrainingType']"})
        },
        u'feedback.formquestionanswer': {
            'Meta': {'object_name': 'FormQuestionAnswer', 'db_table': "u'form_question_answer'", 'managed': 'False'},
            'answer_offered_id': ('django.db.models.fields.IntegerField', [], {}),
            'form_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'feedback.question': {
            'Meta': {'object_name': 'Question', 'db_table': "u'question'", 'managed': 'False'},
            'question': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'question_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'feedback.role': {
            'Meta': {'object_name': 'Role', 'db_table': "u'role'", 'managed': 'False'},
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'role_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'technical': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'feedback.southmigrationhistory': {
            'Meta': {'object_name': 'SouthMigrationhistory', 'db_table': "u'south_migrationhistory'", 'managed': 'False'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'applied': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'migration': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'feedback.trainingtype': {
            'Meta': {'object_name': 'TrainingType', 'db_table': "u'training_type'", 'managed': 'False'},
            'training_type_desc': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'training_type_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['feedback']