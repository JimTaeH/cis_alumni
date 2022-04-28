from django.shortcuts import render
from logging import exception
from unicodedata import category
from django.shortcuts import render, redirect
from .forms import NewUserForm, UserForm
from django.contrib import messages #import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from alumnidata.models import Profile, fieldstudy, job, education, success

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
	uproflie = Profile.objects.get(user=request.user)

	context = {
		'user': request.user,
		'profile': uproflie,
		'user_id': request.user.id,
	}

	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)

		if user_form.is_valid():
			user_form.save()
			messages.success(request,('Your profile was successfully updated!'))
			
		else:
			messages.error(request,('Unable to complete request here'))
			return redirect (f"/user/{request.user.id}/")

		if 'role' in request.POST:
			role = request.POST['role']
			user_profile = Profile.objects.get(user=request.user)
			user_profile.role = role
			user_profile.save()
			return redirect (f"/user/{request.user.id}/")
		else:
			messages.error(request,('Unable to update role'))
			return redirect (f"/user/{request.user.id}/")
	
	return render(request, 'userpage.htm', context)

def fieldstudy_page(request, id):
	uproflie = Profile.objects.get(user=request.user)

	if fieldstudy.objects.filter(alumniuser=uproflie).count() != 0:
		ufofs = fieldstudy.objects.get(alumniuser=uproflie)
	else:
		ufofs = None

	context = {
		'profile': uproflie,
		'user_id': request.user.id,
		'ufofs': ufofs,
	}

	if request.method == "POST":
		studyField = request.POST['studyField']
		major = request.POST['major']
		minor = request.POST['minor']
		start = request.POST['start']
		stop = request.POST['stop']
		gpa = request.POST['gpa']

		if fieldstudy.objects.filter(alumniuser=uproflie).count() == 0:
			fofstudy = fieldstudy.objects.create(alumniuser=uproflie)
			fofstudy.studyField = studyField
			fofstudy.studyMajor = major
			fofstudy.studyMinor = minor
			fofstudy.yearStart = start
			fofstudy.yearGraduate = stop
			fofstudy.gpa = gpa
			fofstudy.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/fofs/{request.user.id}/")

		elif fieldstudy.objects.filter(alumniuser=uproflie).count() != 0:
			fofstudy = fieldstudy.objects.get(alumniuser=uproflie)
			fofstudy.studyField = studyField
			fofstudy.studyMajor = major
			fofstudy.studyMinor = minor
			fofstudy.yearStart = start
			fofstudy.yearGraduate = stop
			fofstudy.gpa = gpa
			fofstudy.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/fofs/{request.user.id}/")
		
		else:
			messages.error(request,('Unable to update your data'))
			return redirect (f"/fofs/{request.user.id}/")

	return render(request, 'fieldstudy.htm', context)

def job_page(request, id):
	uproflie = Profile.objects.get(user=request.user)

	if job.objects.filter(alumniuser=uproflie).count() != 0:
		ujob = job.objects.get(alumniuser=uproflie)
	else:
		ujob = None

	context = {
		'profile': uproflie,
		'user_id': request.user.id,
		'ujob': ujob,
	}

	if request.method == "POST":
		organization = request.POST['organization']
		organizationType = request.POST['organizationType']
		department = request.POST['department']
		jobTitle = request.POST['jobTitle']
		jobDesc = request.POST['jobDesc']

		if job.objects.filter(alumniuser=uproflie).count() == 0:
			alumnijob = job.objects.create(alumniuser=uproflie)
			alumnijob.organization = organization
			alumnijob.organizeType = organizationType
			alumnijob.department = department
			alumnijob.jobTitle = jobTitle
			alumnijob.jobDesc = jobDesc
			alumnijob.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/job/{request.user.id}/")

		elif job.objects.filter(alumniuser=uproflie).count() != 0:
			alumnijob = job.objects.get(alumniuser=uproflie)
			alumnijob.organization = organization
			alumnijob.organizeType = organizationType
			alumnijob.department = department
			alumnijob.jobTitle = jobTitle
			alumnijob.jobDesc = jobDesc
			alumnijob.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/job/{request.user.id}/")
		
		else:
			messages.error(request,('Unable to update your data'))
			return redirect (f"/job/{request.user.id}/")

	return render(request, 'job.htm', context)

def education_page(request, id):
	uproflie = Profile.objects.get(user=request.user)

	if education.objects.filter(alumniuser=uproflie).count() != 0:
		ueducation = education.objects.get(alumniuser=uproflie)
	else:
		ueducation = None

	context = {
		'profile': uproflie,
		'user_id': request.user.id,
		'uedu': ueducation,
	}

	if request.method == "POST":
		degree = request.POST['degree']
		university = request.POST['university']
		faculty = request.POST['faculty']
		major = request.POST['major']
		country = request.POST['country']

		if education.objects.filter(alumniuser=uproflie).count() == 0:
			alumnieducation = education.objects.create(alumniuser=uproflie)
			alumnieducation.degree = degree
			alumnieducation.university = university
			alumnieducation.faculty = faculty
			alumnieducation.major = major
			alumnieducation.country = country
			alumnieducation.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/education/{request.user.id}/")

		elif education.objects.filter(alumniuser=uproflie).count() != 0:
			alumnieducation = education.objects.get(alumniuser=uproflie)
			alumnieducation.degree = degree
			alumnieducation.university = university
			alumnieducation.faculty = faculty
			alumnieducation.major = major
			alumnieducation.country = country
			alumnieducation.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/education/{request.user.id}/")
		
		else:
			messages.error(request,('Unable to update your data'))
			return redirect (f"/education/{request.user.id}/")

	return render(request, 'education.htm', context)

def achievement_page(request, id):
	uproflie = Profile.objects.get(user=request.user)

	if success.objects.filter(alumniuser=uproflie).count() != 0:
		usuccess = success.objects.get(alumniuser=uproflie)
	else:
		usuccess = None

	context = {
		'profile': uproflie,
		'user_id': request.user.id,
		'usuccess': usuccess
	}

	if request.method == "POST":
		title = request.POST['title']
		achievedate = request.POST['achievedate']
		desc = request.POST['desc']

		if success.objects.filter(alumniuser=uproflie).count() == 0:
			alumnisuccess = success.objects.create(alumniuser=uproflie)
			alumnisuccess.title = title
			alumnisuccess.achievedate = achievedate
			alumnisuccess.desc = desc
			alumnisuccess.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/achievement/{request.user.id}/")

		elif success.objects.filter(alumniuser=uproflie).count() != 0:
			alumnisuccess = success.objects.get(alumniuser=uproflie)
			alumnisuccess.achieveTitle = title
			alumnisuccess.achieveDate = achievedate
			alumnisuccess.desc = desc
			alumnisuccess.save()
			messages.success(request,('Your data was successfully updated!'))
			return redirect (f"/achievement/{request.user.id}/")
		
		else:
			messages.error(request,('Unable to update your data'))
			return redirect (f"/achievement/{request.user.id}/")

	return render(request, 'achievement.htm', context)