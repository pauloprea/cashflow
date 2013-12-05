# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AccountOperation.description'
        db.alter_column(u'cashflow_accountoperation', 'description', self.gf('django.db.models.fields.TextField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'AccountOperation.description'
        db.alter_column(u'cashflow_accountoperation', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

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
        u'cashflow.account': {
            'IBAN': ('django_iban.fields.IBANField', [], {'max_length': '34', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Account'},
            'SWIFTBIC': ('django_iban.fields.SWIFTBICField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashflow.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'cashflow.accountoperation': {
            'Meta': {'object_name': 'AccountOperation'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashflow.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 12, 5, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_cashflow.accountoperation_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'stamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'null': 'True'})
        },
        u'cashflow.currency': {
            'Meta': {'object_name': 'Currency'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'cashflow.income': {
            'Meta': {'object_name': 'Income', '_ormbases': [u'cashflow.AccountOperation']},
            u'accountoperation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cashflow.AccountOperation']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cashflow.payment': {
            'Meta': {'object_name': 'Payment', '_ormbases': [u'cashflow.AccountOperation']},
            u'accountoperation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cashflow.AccountOperation']", 'unique': 'True', 'primary_key': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cashflow.Currency']", 'null': 'True', 'blank': 'True'}),
            'currency_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'cashflow.transferin': {
            'Meta': {'object_name': 'TransferIn', '_ormbases': [u'cashflow.AccountOperation']},
            u'accountoperation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cashflow.AccountOperation']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cashflow.transferout': {
            'Meta': {'object_name': 'TransferOut', '_ormbases': [u'cashflow.AccountOperation']},
            u'accountoperation_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cashflow.AccountOperation']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cashflow']