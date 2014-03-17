from decimal import *
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from enums import general_enums
import calendar

def datetime_to_unix_ms(dt):
	return calendar.timegm(dt.utctimetuple())


def datetime_to_ms(dt):
	"""
	returns milliseconds since Jan 1, 1970
	"""
	base = datetime_from_string('19700101')
	td = dt - base
	ms = td.total_seconds()*1000
	return ms

def datetime_to_string(datetime_, split=False, reverse=True, easy=False):
	"""
		Turns a datetime object into a string of the form
		easy = True uses datetime.strftime('%d-%m-%Y %X') which gives the appropriate date and time representation for Locale.
			e.g. Wed Dec 25 17:15:30 201
		reverse = True: YYYYMMDD or YYYY-MM-DD depending on whether split is False or True (respectively)
		reverse = False: DDMMYYYY or DD-MM-YYYY depending on whether split is False or True (respectively)
	"""
	if easy:
		return datetime_.strftime('%d-%m-%Y %X')

	if split:
		if reverse:
			return datetime_.strftime('%Y-%m-%d')
		else:
			return datetime_.strftime('%d-%m-%Y')

	else:
		if reverse:
			return datetime_.strftime('%Y%m%d')
		else:
			return datetime_.strftime('%d%m%Y')


def datetime_from_string(string_, split=False, reverse=True, easy=False):
	"""
		Turns a string of the form specified into datetime object
		easy = True uses datetime.strptime('%d-%m-%Y %X') which assumes string_ has the appropriate date and time
			representation for Locale. e.g. Wed Dec 25 17:15:30 201
		reverse = True: YYYYMMDD or YYYY-MM-DD depending on whether split is False or True (respectively)
		reverse = False: DDMMYYYY or DD-MM-YYYY depending on whether split is False or True (respectively)
	"""

	if easy:
		return datetime.strptime(string_, '%d-%m-%Y %X')

	if split:
		if reverse:
			return datetime.strptime(string_, '%Y-%m-%d', )
		else:
			return datetime.strptime(string_, '%d-%m-%Y')

	else:
		if reverse:
			return datetime.strptime(string_, '%Y%m%d')
		else:
			return datetime.strptime(string_, '%d%m%Y')


def periods_between_datetimes(datetime_1, datetime_2=datetime.now(), period='M'):
	"""
	For any two datetime objects find the number of periods between them,
	period: accepts any period listed in general_enums.time_periods

	IMPORTANT: will return decimal values, does not necessarily return whole numbers
	"""

	reference = general_enums.time_period_conversions

	if period in reference.keys():

		most_recent = max([datetime_1, datetime_2])
		least_recent = min([datetime_1, datetime_2])

		# print most_recent, least_recent

		if period == 'Y':
			return Decimal(
				(most_recent.year - least_recent.year) + Decimal(most_recent.month - least_recent.month) / 12.0)

		elif period == 'Q':
			return Decimal(
				((most_recent.month - least_recent.month) + (most_recent.year - least_recent.year) * 12.0) / 3.0)

		elif period == 'M':
			return Decimal(((most_recent.month - least_recent.month) + (most_recent.year - least_recent.year)) * 12.0)

		else:
			difference = most_recent - least_recent
			days = difference.days

			if period == 'W':
				return Decimal((days) / 7.0)
			else:
				return Decimal(days)
	else:

		return False


def timestep(steps, periodicity):
	"""
	Returns relative delta for number of steps of a given period (periodicity)
	"""
	if periodicity == 'D':
		return relativedelta(days=steps)
	elif periodicity == 'W':
		return relativedelta(days=7 * steps)
	elif periodicity == 'M':
		return relativedelta(months=steps)
	elif periodicity == 'Q':
		return relativedelta(months=3 * steps)
	elif periodicity == 'Y':
		return relativedelta(years=steps)
	else:
		return relativedelta(days=0) # Invalid input)


def time_of_day(dt):
	"""
	Returns time of day for a time or datetime object
	morning, afternoon, evening, night, late night for
	0400-1200, 1200-1700, 1700-2100,2100-0000,0000-0400

	CRW: Would it not make more sense to have 4 equal 
	periods: morning(0600-1200), afternoon(1200-1800), 
	evening(1800-0000), night(0000-0600)? Rather than 
	4 evening periods and a massive morning period
	"""
	r = {}
	the_time_of_day = ''

	try:
		h = dt.hour

		if h < 4:
			the_time_of_day = 'late night'
		elif h < 12:
			the_time_of_day = 'morning'
		elif h < 14:
			the_time_of_day = 'lunchtime'
		elif h < 17:
			the_time_of_day = 'late afternoon'
		elif h < 21:
			the_time_of_day = 'evening'
		else:
			the_time_of_day = 'night'

		r = {'error_code': '',
			 'return_value': the_time_of_day,
		}

	except Exception, e:
		r = {'error_code': e,
			 'return_value': 'error',
		}

	return r


def get_weekday(dt):
	"""
	Returns day of week for a datetime object
	"""

	try:
		r = {
		'error_code': '',
		'return_value': zip(*general_enums.days_of_week)[1][dt.isoweekday() - 1],
		}
	except Exception, e:
		r = {
		'error_code': e,
		'return_value': 'error',
		}

	return r


zodiacs = [(1220, 'Sag'), (118, 'Cap'), (220, 'Aqu'), (320, 'Pis'), (421, 'Ari'),
		   (521, 'Tau'), (622, 'Gem'), (723, 'Can'), (823, 'Leo'), (923, 'Vir'),
		   (1022, 'Lib'), (1122, 'Scorp'), (131, 'Sag')]
def get_zodiac(dt):
	date_number = int("".join((str(dt.date().month), '%02d' % dt.date().day)))
	for z in zodiacs:
		if date_number < z[0]:
			return z[1]

def get_month(dt):
	"""
	INPUT: <datetime object>
	RETURN: <string> of month
	"""
	r = {}
	month = ''

	try:
		m = dt.month

		if m == 1 :
			month = 'January'
		elif m == 2 :
			month = 'February'
		elif m == 3 :
			month = 'March'
		elif m == 4 :
			month = 'April'
		elif m == 5 :
			month = 'May'
		elif m == 6 :
			month = 'June'
		elif m == 7 :
			month = 'July'
		elif m == 8 :
			month = 'August'
		elif m == 9 :
			month = 'September'
		elif m == 10 :
			month = 'October'
		elif m == 11 :
			month = 'November'
		elif m == 12 :
			month = 'December'


		r = {'error_code': '',
			 'return_value': month,
		}

	except Exception, e:
		r = {'error_code': e,
			 'return_value': 'error',
		}

	return r