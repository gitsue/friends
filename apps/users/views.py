from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from.models import User
from django.contrib import messages
# Create your views here.
def index(request):
	if "user_id" in request.session:
		return redirect("friend:index")
	else:	
		return render(request, "index.html")	

def register(request):
	if request.method =="POST":
		result = User.usermgr.register(request.POST)
	if result['registered']:
		request.session["user_id"] = result["user"].id
		return redirect ("users:success")
	else:
		for error in result['errors']:
			messages.add_message(request, messages.INFO, error)
		return redirect(reverse("users:index"))

def login(request):
	if request.method =="POST":
		result = User.usermgr.login(request.POST)
	if result:
		request.session["user_id"] = result.id
		return redirect ("users:success")
	else:
		messages.add_message(request, messages.INFO, "Invalid email/password.")
		return redirect(reverse("users:index"))

def success(request):
	return redirect(reverse("friend:index"))

def logout(request):
	request.session.clear()
	return redirect(reverse("users:index"))