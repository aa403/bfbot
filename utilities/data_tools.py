import base64
import numpy as np
import re
from collections import OrderedDict
from operator import itemgetter, attrgetter
from datetime import datetime


try:
	import simplejson as json
except ImportError:
	import json

from enums import general_enums

def cumulative(iterable):
	return [sum(iterable[:i+1]) for i in xrange(len(iterable))]

def extent(iterable):
	return (float(min(iterable)),float(max(iterable)))

def domain_to_range(val, domain, codomain):
	"""
	maps val from domain to range
	@param val: float
	@param domain: if number, converted to range, if list, take extent
	@param codomain: (a.k.a range) if number, converted to range, if list, take extent
	@return:
	"""

	def get_range(v):
		if isinstance(v, (int, float)):
			v = extent((0,v))
		elif isinstance(v, (list,tuple)):
			v = extent(v)
		return v

	val = float(val)

	domain = get_range(domain)
	domain_len = domain[1] - domain[0]

	codomain = get_range(codomain)
	codomain_len = codomain[1] - codomain[0]

	scale = float(codomain_len) / domain_len

	return ((val - domain[0]) * scale) + codomain[0]


def tuples_to_lists(tuples):
	""" Turns all of the tuples in any structure of tuples and lists into lists """
	return list(map(tuples_to_lists(), tuples)) if isinstance(tuples, (list, tuple)) else tuples


def get_ordered_list_by_key(list, key_string, reverse=False):
	""" Sorts a list by a specified key_string"""
	try:
		return sorted(list, key=itemgetter(key_string), reverse=reverse)
	except:
		return sorted(list, key=attrgetter(key_string), reverse=reverse)


def ordered_set(original_list):
	"""
	Takes original_list, creates an ordered dict, then converts back to list

	"""
	return list(OrderedDict.fromkeys(original_list))


def find_in_tuple(tuple_list, lookup, lookup_col=0, search_col=1):
	"""
	Find value in list or tuple of tuples. Very similar to excel VLOOKUP()
	the 'lookup' argument is matched in the lookup_col, and
	the appropriate value in the search_col is returned
	"""
	zipped_tuple = zip(*tuple_list)

	try:
		return zipped_tuple[search_col][zipped_tuple[lookup_col].index(lookup)]

	except ValueError:
		return {'error_code': 0, 'error_value': 'nothing found'}  # maybe this should be False?


def ordered_set_from_list_of_pairs(originalList):
	new_rels = []

	keys = zip(*originalList)[0]

	pairVals = zip(*originalList)[1]

	for counter, x in enumerate(keys):
		if new_rels == []:
			new_rels.append([x, pairVals[counter]])

		elif x not in zip(*new_rels)[0]:
			new_rels.append([x, pairVals[counter]])

	return new_rels

def as_json(input, indent=0):
	""" Will convert a Python dictionary into a JSON object.
		Conversion is first attempted using simplejson, if this does not work then json will be used.

		INPUTS: <Python dict>
		OUTPUTS: <JSON object>

	"""
	
	return json.dumps(convert_datetimes_in_dictionary(input), indent=indent, sort_keys=True)

def convert_datetimes_in_dictionary(dictionary):
	for k, v in dictionary.iteritems():
		if isinstance(v, datetime):
			dictionary[k] = v.strftime('%c')

		elif isinstance(v, dict):
			dictionary[k] = convert_datetimes_in_dictionary(v)

	return dictionary


def from_json(input):
	""" Will convert a JSON object into a Python dictionary .
		Conversion is first attempted using simplejson, if this does not work then json will be used.

		INPUTS: <JSON object>
		OUTPUTS: <Python dict>

	"""
	try:
		return json.load(input)
	except:
		return json.loads(input)


def bool_to_english(bool_value):
	""" Converts the bool True into the string "Yes" and the bool False, into the string "No".
		In this instance bool includes any boolean string variable from enums.BOOL_TRUES.

		Any null or non-boolean/enums.BOOL_TRUES value will produce a "No".

		INPUTS: <boolean or enums.BOOL_TRUES>
		OUTPUT: <string "Yes" or "No">
	"""
	if bool_value in general_enums.BOOL_TRUES:
		return "Yes"

	else:
		return "No"


def underscores_to_spaces(word_with_underscores):
	"""
	This function removes underscores from a word and replaces them with spaces:
	the_test_Word_IS__this -> the test Word IS  this
	with no other changes involved
	"""
	return re.sub('_', r' ', word_with_underscores)


def spaces_to_underscores(word_with_underscores):
	"""
	This function removes underscores from a word and replaces them with spaces:
	the_test_Word_IS__this -> the test Word IS  this
	with no other changes involved
	"""
	return re.sub(' ', r'_', word_with_underscores)


def remove_spaces(name):
	""" returns value of string with underscores replaced with spaces """
	return name.replace(' ', '')


def str_to_number(number, dp=None):
	"""
	Take a string and try to turn it into a float, then an int. If successful at either step return the float or int value.
	 Use dp to set number or
	"""

	numType = 'str'

	try:
		float(number)
		numType = 'fl'

	except ValueError:
		return str(number)

	except TypeError:
		return None

	if numType == 'fl':
		try:
			int(number)
			return int(number)

		except ValueError:
			if dp:
				return round(float(number), dp)
			else:
				return float(number)

	else:
		return {'error': 'numType = str'}


def encode_list_or_array(data):
	if isinstance(data, list):
		data = np.array(data)

	return base64.b64encode(data.astype(np.float64))


def decode_to_array(data):
	return np.frombuffer(base64.decodestring(data), dtype=np.float64)


from django.utils.encoding import smart_str


def _smart_key(key):
	return smart_str(''.join([c for c in key if ord(c) > 32 and ord(c) != 127]))


def make_key(key, key_prefix='', version=''):
	"Truncate all keys to 250 or less and remove control characters"
	return ':'.join([key_prefix, str(version), _smart_key(key)])[:250]

def aggregate_coordinates_with_weighting(anchor_locations_list):
		"""
			coords should be a list of coordinates each set of which should be a tuple of the form:
			self.anchor_locations_list = [(latitude, longitude, weighting),...]
		"""

		if len(anchor_locations_list) > 0:
			total_weight = sum(zip(*anchor_locations_list)[2]) # sum([c[2] for c in self.anchor_locations_list])
			if total_weight != 0:

				latitude, longitude = 0, 0

				for c in anchor_locations_list:

					latitude += c[0] * float(c[2])/total_weight

					longitude += c[1] * float(c[2])/total_weight

				return (latitude, longitude)
			else:
				return None

		else:
			return None