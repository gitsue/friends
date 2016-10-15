from django.shortcuts import render, redirect
from ..users.models import User
from .models import Friend
# Create your views here.
def index(request):
	context = {
		"curr_user": User.usermgr.filter(id=request.session["user_id"]),
		"other_users": User.usermgr.exclude(id=request.session["user_id"]),
		"friendlist": Friend.friendmgr.filter(user=request.session["user_id"])
	}
	print context['friendlist']
	return render(request, "friendlist/index.html", context)

def addfriend(request, user_id):
	Friend.friendmgr.addfriend(request.session["user_id"], user_id)
	return redirect("friendlist:index")

def removefriend(request):
	pass

def profilepage(request, user_id):
	context = {
		"user": User.usermgr.filter(id=user_id),
	}
	return render(request, "friendlist:show", context)
