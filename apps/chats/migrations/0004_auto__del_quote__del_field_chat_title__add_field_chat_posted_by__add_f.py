# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Quote'
        db.delete_table('chats_quote')

        # Removing M2M table for field friend_groups on 'Quote'
        db.delete_table('chats_quote_friend_groups')

        # Deleting field 'Chat.title'
        db.delete_column('chats_chat', 'title')

        # Adding field 'Chat.posted_by'
        db.add_column('chats_chat', 'posted_by', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['auth.User']), keep_default=False)

        # Adding field 'Chat.text'
        db.add_column('chats_chat', 'text', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding M2M table for field friend_groups on 'Chat'
        db.create_table('chats_chat_friend_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chat', models.ForeignKey(orm['chats.chat'], null=False)),
            ('friendgroup', models.ForeignKey(orm['profiles.friendgroup'], null=False))
        ))
        db.create_unique('chats_chat_friend_groups', ['chat_id', 'friendgroup_id'])


    def backwards(self, orm):
        
        # Adding model 'Quote'
        db.create_table('chats_quote', (
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('chat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chats.Chat'], null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('chats', ['Quote'])

        # Adding M2M table for field friend_groups on 'Quote'
        db.create_table('chats_quote_friend_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quote', models.ForeignKey(orm['chats.quote'], null=False)),
            ('friendgroup', models.ForeignKey(orm['profiles.friendgroup'], null=False))
        ))
        db.create_unique('chats_quote_friend_groups', ['quote_id', 'friendgroup_id'])

        # User chose to not deal with backwards NULL issues for 'Chat.title'
        raise RuntimeError("Cannot reverse this migration. 'Chat.title' and its values cannot be restored.")

        # Deleting field 'Chat.posted_by'
        db.delete_column('chats_chat', 'posted_by_id')

        # Deleting field 'Chat.text'
        db.delete_column('chats_chat', 'text')

        # Removing M2M table for field friend_groups on 'Chat'
        db.delete_table('chats_chat_friend_groups')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chats.chat': {
            'Meta': {'object_name': 'Chat'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'friend_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['profiles.FriendGroup']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.friendgroup': {
            'Meta': {'object_name': 'FriendGroup'},
            'admins': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['chats']
