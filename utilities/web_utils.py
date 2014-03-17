__author__ = 'Ammar Akhtar'
import urllib2
import urllib
import httplib
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import validations
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def open_url(url, data=None, request_type='POST'):
			"""
			Returns as text the content of the url supplied
			use data to specify queries for POST / GET, as a dictionary (defaults to none)
			use request_type to specify GET or POST (defaults to POST)
			"""


			if request_type not in ['GET', 'POST']:
				request_type = 'POST'


			if validations.is_empty_or_false(data):
				data = {}

			elif not isinstance(data, dict):
				return {'return_value':'url parameters not supplied as dictionary',
					'error_code': '0'}

			#user_agent = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
			#headers = {'User-Agent' : user_agent}

			if request_type == 'POST':
				req = urllib2.Request(url, urllib.urlencode(data))

			elif request_type == 'GET':
				url = url + '?' + urllib.urlencode(data)
				req = urllib2.Request(url)


			try:
				response = urllib2.urlopen(req)
				error_code = ''
			except urllib2.HTTPError, e:
				response = e
				error_code = 'HTTPError'
			except urllib2.URLError, e:
				response = e
				error_code = 'URLError'
			except httplib.HTTPException, e:
				response = e
				error_code = 'HTTPException'
			except Exception, e:
				import traceback
				# response = 'generic exception: ' + traceback.format_exc()
				response = e
				error_code = 'Generic Exception'


			return {'return_value':response, 'error_code': error_code}
