__author__ = 'ammarorama'

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from bfbot.keys import live, delayed, endpoint
import urllib, urllib2
import json

@login_required
def firstpage(request):
	template = 'bfbot_core/main.html'
	context ={
		'hello':'hello, world',
	}
	return render(request, template, context)


def getResponseFromPost(url, data, headers={}, formencoded=False):

	if formencoded == True:
		req = urllib2.Request(url, urllib.urlencode(data))
	else:
		req = urllib2.Request('{}?{}'.format(url, urllib.urlencode(data)), headers=headers)

	return urllib2.urlopen(req)


def testConnection(request):
	template = 'bfbot_core/main.html'

	# endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0"

	url = endpoint #+ "listEventTypes/"

	header = { 'X-Application' : live,
	         'X-Authentication' : 'ivku1hEDNZxu7n1nDQkHPg6QVh9XsIFRnbbc4KqMzRI=' ,
			 'content-type' : 'application/json' }

	json_req='{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEventTypes", "params": {"filter":{ }}, "id": 1}'


	# data = urllib.urlencode(json_req)
	req = urllib2.Request(url, json_req, headers=header)

	response = urllib2.urlopen(req)

	# response = getResponseFromPost(url,data=json_req, headers=header)
	# response = requests.post(url, data=json_req, headers=header)

	context = {'hello':response.read()}
	# print json.dumps(json.loads(response.read()), indent=3)
	return render(request, template, context)