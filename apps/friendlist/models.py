from __future__ import unicode_literals
from django.db import models
from ..users.models import User
# Create your models here.

class FriendManager(models.Manager):
	def addfriend(self, user_id, friend_id):
		user_id = User.usermgr.get(id=user_id)
		friend_id = User.usermgr.get(id=friend_id)
		user_id.friend_set.add(friend_id.id)
		user_id.save()

	def removefriend(self):
		pass

class Friend(models.Model):
	user = models.ManyToManyField(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	friendmgr = FriendManager()