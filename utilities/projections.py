__author__ = 'krhn'
# from dateutil.relativedelta import relativedelta
from operator import mul
from copy import deepcopy

# import rates as baserates



def format_rates_list(rates_list, number_of_periods=0, compounded_rates=True, additive_not_multiplicative=True):
	""" Takes any rates_list and forces it into a compounded, multiplicative list of rates of the desired length

		INPUTS: rates_list - the original list of float values
				number_of_periods - how long the list needs to be
				compounded_rates - is the original data already compounded? True for compounded
				additive_not_multiplicative - is the original data additive (i.e. 0.0x) or multi (i.e. 1.0x)? True for additive

		OUTPUTS: A single list of floats of the appropriate format as discussed above

		IMPORTANT: Missing data is always extrapolated linearly from the point at which data is missing

	"""

	number_of_rates = len(rates_list)

	if not isinstance(number_of_periods, int) or number_of_periods == 0:
		number_of_periods = number_of_rates

	if number_of_periods <= number_of_rates and compounded_rates and additive_not_multiplicative == False:
		return rates_list[:number_of_periods] # it's already in the right format
		#return rates_list # it's already in the right format

	elif number_of_rates == 1: # if there's just a single rate extrapolate it out as required and then return
		if additive_not_multiplicative:
			return [(rates_list[0] + 1.0) ** (i + 1) for i in xrange(number_of_periods)]
			# add 1.0 if it is additive to make it multiplicative before extrapolating (compounding)
		else:
			return [rates_list[0] ** (i + 1) for i in xrange(number_of_periods)]

	elif compounded_rates: # if it is already compounded
		if additive_not_multiplicative:
			output = [rate + 1.0 for rate in rates_list]
			# add 1.0 if additive
		else:
			output = rates_list
			# if it's already multiplicative and compounded then it's just a case of ensuring length (below)
	else: # needs compounding
		if additive_not_multiplicative:
			adjusted_rates = [rate + 1.0 for rate in rates_list]
			output = [reduce(mul, adjusted_rates[:i], 1.0) * adjusted_rates[i] for i in xrange(number_of_rates)]
			# each element of the output is a compound of all the previous elements + 1.0
		else:
			output = [reduce(mul, rates_list[:i], 1.0) * rates_list[i] for i in xrange(number_of_rates)]
			# already multiplicative so each element is just a compound of all the previous elements

	if number_of_rates >= number_of_periods: # if the length is sufficient then we are done
		return output[:number_of_periods]

	else: # otherwise we need to extrapolate out the missing data, which will be done in a universal way
	# now that the data is formatted
		j = 0 # counter
		formatted_rates = deepcopy(output) # for reference

		while number_of_rates + j < number_of_periods: # until we have enough datapoints
			output.append(((formatted_rates[-1] / formatted_rates[-2]) ** (j + 1)) * formatted_rates[-1])
			j += 1
			# compound the linear difference in the last 2 real datapoints and add it to the output

		return output


def project_single_value_with_formatted_rates(formatted_rates, initial_value):
	"""
	Projection for the initial value using the list of formatted rates (assumed to be the term rates)
	"""
	return [rate * initial_value for rate in [1.0] + formatted_rates]


def project_list_values_with_formatted_rates(formatted_rates, initial_list):
	"""
	Projection for each value in initial value list, using the list of formatted rates (assumed to be the term rates)
	"""
	return [formatted_rates[i] * initial_list[i] for i in xrange(min(len(initial_list), len(formatted_rates)))]


def project_value_generic(initial_value, rates_list, number_of_periods, compounded_rates=True,
                          additive_not_multiplicative=True):
	formatted_rates = format_rates_list(rates_list, number_of_periods, compounded_rates, additive_not_multiplicative)

	return project_single_value_with_formatted_rates(formatted_rates, initial_value)


def project_value_generic_list(initial_list, rates_list, number_of_periods, compounded_rates=True,
                               additive_not_multiplicative=True):
	formatted_rates = format_rates_list(rates_list, number_of_periods, compounded_rates, additive_not_multiplicative)

	return project_list_values_with_formatted_rates(formatted_rates, initial_list)


# def project_value_for_rate_type(initial_value, rate_type, start_datetime, end_datetime, periodicity='M', nominal=False,
#                                 compound=True, round_up=True):
# 	""" Choose rate_type to project initial value from, start_datetime should be the initial_value at date of valuation rather than datetime.now()
#
# 		Advise not to override any of the defaulted fields unless you're 100% sure it's necessary for your calculation
#
# 	"""
#
# 	rates_list = baserates.get_curve(rate_type, start_datetime, end_datetime, periodicity, nominal, compound, round_up)
# 	# Pretty sure this should be effective not nominal but review later
#
# 	return project_value_generic(initial_value, rates_list, len(rates_list), True, True)
# 	# current get_curve outputs additive, revise this if that changes
#
#
# def project_value_for_rate_type_list(initial_list, rate_type, start_datetime, end_datetime, periodicity='M',
#                                      nominal=False, compound=True, round_up=True):
# 	""" Choose rate_type to project initial value from, start_datetime should be the initial_value at date of valuation rather than datetime.now()
#
# 		Advise not to override any of the defaulted fields unless you're 100% sure it's necessary for your calculation
#
# 	"""
#
# 	rates_list = baserates.get_curve(rate_type, start_datetime, end_datetime, periodicity, nominal, compound, round_up)
# 	# Pretty sure this should be effective not nominal but review later
#
# 	return project_value_generic_list(initial_list, rates_list, len(rates_list), True, True)
# 	# current get_curve outputs additive, revise this if that changes