# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Wine.slug'
        db.add_column(u'corewine_wine', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='test', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Wine.slug'
        db.delete_column(u'corewine_wine', 'slug')


    models = {
        u'corewine.acidity': {
            'Meta': {'object_name': 'Acidity'},
            'acidity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.aroma': {
            'Meta': {'object_name': 'Aroma'},
            'aroma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'corewine.cepage': {
            'Meta': {'object_name': 'Cepage'},
            'cepage': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 25, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 25, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'})
        },
        u'corewine.tag': {
            'Meta': {'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 25, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 25, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '60'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.tanin': {
            'Meta': {'object_name': 'Tanin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'tanin': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'corewine.taste': {
            'Meta': {'object_name': 'Taste'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'taste': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'corewine.teint': {
            'Meta': {'object_name': 'Teint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'teint': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'corewine.wine': {
            'Meta': {'object_name': 'Wine'},
            'acidity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Acidity']"}),
            'alcool': ('django.db.models.fields.FloatField', [], {}),
            'appelation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'aroma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Aroma']"}),
            'cepage': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['corewine.Cepage']", 'symmetrical': 'False'}),
            'code_saq': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 25, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 25, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'mouth_intensity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'nose_intensity': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'persistance': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['corewine.Tag']", 'null': 'True', 'blank': 'True'}),
            'tanin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Tanin']", 'blank': 'True'}),
            'taste': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Taste']"}),
            'teint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['corewine.Teint']"}),
            'wineType': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['corewine']