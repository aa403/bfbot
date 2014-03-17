import math

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from utilities import validations
from utilities.data_tools import underscores_to_spaces
from enums import general_enums


register = template.Library()


@register.filter
def dateForDateInput(dt):
	# print str(dt)
	r = dt

	return r

@register.filter
def condense(str):
	"""
	if str = "My House"; returns "myHouse"
	"""

	str = str[0].lower() + str[1:]
	return str.replace(" ","")




@register.filter
def ends_in(item, char):
	return item.endswith(char);

@register.filter
def sterling(val):
	if isinstance(val, (int, float)):
		return u'\u00A3'+str(intcomma(val))
	else:
		return val;

@register.filter
def currency(val, type):
	if isinstance(val, (int, float)):
		if type == "pound" or type == "sterling" or type == "quid":
			return u'\u00A3'+str(intcomma(val))
		elif type == "dollars":
			return u'\u0024'+str(intcomma(val))	
		else:
			return val;	
	else:
		return val;

@register.filter
def in_list(value, arg):
  """
  Given an item and a list, check if the item is in the list.
  Usage:
  {% if item|in_list:list %} 
      in list 
  {% else %} 
      not in list
  {% endif %}
  """
  return value in arg

@register.filter
def replaceUnderscoresWithSpaces(sentence):
	return underscores_to_spaces(sentence)


@register.filter
def emptyToBlank(item):
	if item in general_enums.empties:
		return ""
	else:
		return item


@register.filter
def is_empty_or_false(item):
	return validations.is_empty_or_false(item)


@register.filter
def not_empty_or_false(item):
	return validations.not_empty_or_false(item)


@register.filter
def getValueFromTupleList(tupleList, lookup):
	keys = zip(*tupleList)[0]
	values = zip(*tupleList)[1]
	r = None

	for k in keys:
		if k == lookup:
			r = values[keys.index(k)]
		else:
			pass

	return r


@register.filter
def relativeToPound(amountSpendPerPound):
	#*2 to get diameter and 50 is radius of smaller circle
	return round((math.sqrt(amountSpendPerPound) * 50) * 2, 2);


@register.filter
def getRange(value):
	r = range(value)
	return r


@register.filter
def getDate(dateTime):
	return dateTime.date()


@register.filter
def get_keys(dictionary):
	return dictionary.keys()


@register.filter
def get_item(dictionary, key):
	return dictionary.get(key, None)


@register.filter
def get_key_and_item(dictionary, key):
	return (key, dictionary.get(key, None))


@register.filter
def get_subDict(dictionary, key):
	#print dictionary, key
	return dictionary.get(key).items()


@register.filter
def len_dict_or_list(dict_or_list):
	return len(dict_or_list)


@register.filter
def getIndex(dict_or_list, index):
	#print index

	return dict_or_list[index]


@register.filter
def negate(value):
	return -value


@register.filter
def remainderIsHalfOrOver(value):
	#says if values decimal point, i.e. remainder, is 0.5 or more 

	#get absolute value
	value = abs(value)

	if value - int(value) - 0.5 >= 0:
		# print "true"
		return True
	else:
		# print "false"
		return False


@register.filter
def round_to(flt, dp):
	# r = locale.format("%.2f", flt, grouping=True)
	#return float("%.2f" % flt)
	return round(float(flt), dp)


@register.filter
def greaterThan(a, b):
	"""
	checks a > b
	"""
	try:
		return a > b
	except:
		return False


@register.filter
def lessThan(a, b):
	"""
	checks a < b
	"""
	try:
		return a < b
	except:
		return False


@register.filter
def equalTo(a, b):
	"""
	checks a == b
	"""
	try:
		return a == b
	except:
		return False


@register.filter
def divideBy(numerator, denominator):
	try:
		r = float(numerator) / denominator
	except:
		r = numerator
	return round(r, 2)


@register.filter
def getAbs(v):
	return round(abs(v))


@register.filter
def multiplyBy(a, b):
	try:
		r = float(a) * b
	except:
		r = a
	return round(r, 2)


@register.filter
def subtract(value, reduce_by):
	return round(float(value) - float(reduce_by), 2)


@register.filter
def parseInt(value):
	try:
		return int(value)
	except:
		return 0
