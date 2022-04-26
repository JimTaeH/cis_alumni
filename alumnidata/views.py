from django.shortcuts import render
from logging import exception
from unicodedata import category
from django.shortcuts import render, redirect
from .forms import NewUserForm, UserForm
from django.contrib import messages #import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from alumnidata.models import Profile

# Create your views here.
def index(request):
	user = request.user
	context = {
		"user_id": user.id
	}
	return render(request, 'index.htm', context)

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request, 'signup.htm', context={"register_form":form})

def login_new(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.htm", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")

def userpage(request, id):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)

		if user_form.is_valid():
			user_form.save()
			messages.success(request,('Your profile was successfully updated!'))
		else:
			messages.error(request,('Unable to complete request'))
			return redirect (f"/user/{request.user.id}/")

		if 'role' in request.POST:
			role = request.POST['role']
			user_profile = Profile.objects.get(user=request.user)
			user_profile.role = role
			user_profile.save()
		else:
			messages.error(request,('Unable to update role'))
			return redirect (f"/user/{request.user.id}/")

		if 'studyField' in request.POST:
			studyField = request.POST['studyField']
			major = request.POST['major']
			minor = request.POST['minor']
			start = request.POST['start']
			stop = request.POST['stop']
			gpa = request.POST['gpa']
		elif not 'studyField' in request.POST:
			pass 
		else:
			messages.error(request,('Unable to update Education 1'))
			return redirect (f"/user/{request.user.id}/")
	
	uproflie = Profile.objects.get(user=request.user)

	context = {
		'user': request.user,
		'profile': uproflie,
		'user_id': request.user.id,
	}
	return render(request, 'userpage.htm', context)