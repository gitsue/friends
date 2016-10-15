from django.shortcuts import render, redirect
from ..users.models import User
from .models import Friend
from django.db.models import Q

# Create your views here.
def index(request):
	context = {
		"curr_user": User.usermgr.filter(id=request.session["user_id"]),
		"friendlist": Friend.fmgr.filter(user=request.session["user_id"]),
		"friendedme": Friend.fmgr.filter(friend = request.session["user_id"]),
		"other_users": User.usermgr.exclude(id=request.session["user_id"]).exclude(friend__user=request.session["user_id"]),
		"friendstable":Friend.fmgr.all
	}
	return render(request, "friend/index.html", context)

def addfriend(request, user_id):
	Friend.fmgr.addfriend(request.session["user_id"], user_id)
	return redirect("friend:index")

def removefriend(request, friend_id):
	Friend.fmgr.removefriend(friend_id)
	return redirect("friend:index")

def profilepage(request, user_id):
	context = {
		"user": User.usermgr.filter(id=user_id),
	}
	return render(request, "friend/show.html", context)