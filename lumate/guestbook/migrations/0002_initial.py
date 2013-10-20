# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guest'
        db.create_table(u'guestbook_guest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('browser_info', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_signed', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'guestbook', ['Guest'])


    def backwards(self, orm):
        # Deleting model 'Guest'
        db.delete_table(u'guestbook_guest')


    models = {
        u'guestbook.guest': {
            'Meta': {'object_name': 'Guest'},
            'browser_info': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_signed': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['guestbook']