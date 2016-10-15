from __future__ import unicode_literals
from django.db import models
import re, bcrypt
import datetime
import time

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def register(self, data):
		errors = []
		curr_date = time.strftime("%Y-%m-%d")
		# print curr_date
		if len(data['name']) < 3 or len(data['alias']) < 3:
			errors.append("Name/Alias need to be greater than 3 characters.")
		if not EMAIL_REGEX.match(data['email']):
			errors.append("Invalid email!")
		if len(data['password']) < 8:
			errors.append("Password should be at least 8 characters.")
		if data['password'] != data['confirmpw']:
			errors.append("Passwords should match!")
		if not data['date']:
			errors.append("Date of birth cannot be blank!")
		if data['date'] > curr_date:
			errors.append("Date of birth cannot be in the future!")
		if data['email'] == User.usermgr.filter(email=data['email']):
			errors.append("Email already registered!")
		# print data['date']
		response = {}

		if errors:
			response['errors'] = errors
			response['registered'] = False
		else:
			response['errors'] = False
			hashedpw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt() )
			user = self.create(name=data['name'], alias=data['alias'], email=data['email'], password = hashedpw, date=data['date'])
			response['user'] = user
			response['registered'] = True
		return response


	def login(self, data):
		user = User.usermgr.filter(email=data['email'])
		if not user:
			return False
		else:
			user = user[0]
		if bcrypt.hashpw(data['password'].encode(), user.password.encode()) == user.password.encode():
			return user
		else:
			return False

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	date = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	usermgr = UserManager()