from __future__ import unicode_literals
from django.db import models
from ..users.models import User
# Create your models here.

class FriendshipManager(models.Manager):
	def addfriend(self, user_id, friend_id):
		user_id = User.usermgr.get(id=user_id)
		friend_id = User.usermgr.get(id=friend_id)
		self.create(user=user_id, friend=friend_id)

	def removefriend(self, friend_id):
		pk_id = Friend.fmgr.get(id=friend_id)
		pk_id.delete()

class Friend(models.Model):
	user = models.ForeignKey(User, related_name="user")
	friend = models.ForeignKey(User, related_name="friend")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	fmgr = FriendshipManager()	