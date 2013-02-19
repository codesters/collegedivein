# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table('college_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('duration', self.gf('django.db.models.fields.SmallIntegerField')(default=3)),
        ))
        db.send_create_signal('college', ['Course'])

        # Adding model 'Address'
        db.create_table('college_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(default='', max_length=350, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('pincode', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='India', max_length=120)),
        ))
        db.send_create_signal('college', ['Address'])

        # Adding model 'CollegeType'
        db.create_table('college_collegetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('college', ['CollegeType'])

        # Adding model 'College'
        db.create_table('college_college', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('college_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.CollegeType'])),
            ('about', self.gf('django.db.models.fields.TextField')(default='')),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.Address'])),
            ('estd', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal('college', ['College'])

        # Adding M2M table for field courses on 'College'
        db.create_table('college_college_courses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('college', models.ForeignKey(orm['college.college'], null=False)),
            ('course', models.ForeignKey(orm['college.course'], null=False))
        ))
        db.create_unique('college_college_courses', ['college_id', 'course_id'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table('college_course')

        # Deleting model 'Address'
        db.delete_table('college_address')

        # Deleting model 'CollegeType'
        db.delete_table('college_collegetype')

        # Deleting model 'College'
        db.delete_table('college_college')

        # Removing M2M table for field courses on 'College'
        db.delete_table('college_college_courses')


    models = {
        'college.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'India'", 'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pincode': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'street': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '350', 'blank': 'True'})
        },
        'college.college': {
            'Meta': {'object_name': 'College'},
            'about': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['college.Address']"}),
            'college_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['college.CollegeType']"}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['college.Course']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'estd': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'college.collegetype': {
            'Meta': {'object_name': 'CollegeType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'college.course': {
            'Meta': {'ordering': "['name']", 'object_name': 'Course'},
            'duration': ('django.db.models.fields.SmallIntegerField', [], {'default': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['college']