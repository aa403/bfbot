__author__ = 'ammarorama'


from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
# from django.template import RequestContext, loader
# from django.core.urlresolvers import reverse
# from django.views import generic
# from django.core.cache import cache
# from django.db.models import Q
from copy import deepcopy

from bfbot_core.models import *




def login(request):

	template = 'welcomepage.html'
	context = {
	'pgtitle':'Log in',
	'abouttitle':"login",
	'aboutpage': "Use this page to login",
	'loginPage': True,
	'hideBar': True
	#'error_type':error_type,
	}
	try:
		context.update({'next_page': str(request.GET['next'])})
	except:
		context.update({'next_page': 'welcomePage'})


	return render(request, template, context)

def do_login(request):

	username = request.POST.get('username', '')
	password = request.POST.get('pw', '')
	next_page = request.POST.get('next_page', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		print "user %s logged in"%user.id
		if user.is_active:
		# Correct password, and the user is marked "active"
			auth.login(request, user)
		# Redirect to a success page.
		#	return redirect('getStarted')
			return redirect(next_page)
		else:
			return redirect('error_page',"user_locked")

	else:
		# Show an error page
		return redirect('error_page',"bad_password_or_no_user")

def do_logout(request):
	u_id = deepcopy(request.user.id)
	auth.logout(request)
	print "user %s logged out"%u_id
	return redirect('login_page')

def create_user(request):
	userName = request.REQUEST.get('username', None)
	userPass = request.REQUEST.get('pw', None)
	userMail = request.REQUEST.get('email', None)
	userFirstName = request.REQUEST.get('firstName', "")
	userLastName = request.REQUEST.get('lastName', "")
	next_page = request.POST.get('next_page', "")


	print userName
	# TODO: check if already existed
	if userName and userPass:

		try:
			u = User.objects.create_user(userName, userMail, userPass)
			created = True


		except IntegrityError:
			u = User.objects.get(username=userName, email=userMail)
			created = False
		print 'created',created

		if created is False:
			return redirect('error_page',"user_already_exists")
			pass
		else:	# user was created
			u.first_name = userFirstName
			u.last_name = userLastName
			u.email = User.objects.normalize_email(userMail)
			u.set_password(userPass)
			u.is_active = True
			u.save()

			user = auth.authenticate(username=userName, password=userPass)
			print user, user.is_active

			if user is not None and user.is_active:
				# Correct password, and the user is marked "active"
				auth.login(request, user)
				# Redirect to a success page.
				return redirect(next_page)

			else:
				return redirect('error_page',"user_locked")

	else:
		return redirect('error_page',"please fill in the form")
		pass


def errorPage(request, error_type):
	template = 'oops.html'

	context = {
	'pgtitle':'Error',
	'abouttitle':"Error",
	'aboutpage': "You are seeing this page because something has gone wrong",
	'error_type':error_type,
	'loginPage': True
	}

	return render(request, template, context)

@login_required
def goToAdmin(request):
	"""
	Redirects to the admin site
	"""

	template = '../admin'
	return HttpResponseRedirect(template)


def root(request):
	"""
	Redirects to the 'welcomePage' landing page
	"""
	template = 'bfbot/main'
	return redirect(template)

def root1(request):
	"""
	Redirects to the 'welcomePage' landing page
	"""
	template = 'main'
	return redirect(template)