# import math
from csv import reader
# from datetime import datetime, timedelta
# import xlrd, xlwt
# from xlwt import *
# from collections import Counter
# from operator import itemgetter
import string
import os

# from ..enums import general_enums
# from ..utilities import datetime_tools
# import re # for regular expressions
# import random

class settingDataFromFiles():
	"""
	This static class will contain all the methods that will allow us to read a file 
	(in CSV format) and store it in some native Python data format, in a sensible way,
	and then to set data attributes equal to these values.

	This will be useful for inputting anything that requires the copying large amounts
	of data from CSV files into Python variable. E.g. the MCC enums variable has 100s
	of data values, these functions will automatically assign those.
	"""

	@staticmethod
	def getCSV(filename):
		"""
		This function will read a CSV in a output it as a list of lists,
		where each element of the list will be a row in the CSV and each
		element of those sublists will be a cell in the original CSV.

		INPUT: <string> filename
		RETURN: <list> of <lists>
		"""

		infile = open(filename, 'r') # open the file in read-only mode

		primary_length = 0
		line_length_flag = False

		file_as_list = [] # initialising an emtpy list to save the fixed CSV in

		for line_literal in reader(infile): # pulling lines out of the statement one-by-one
			line = []
			for element_literal in line_literal:#.encode('utf-8'): 
				element_list = []

				for letter in element_literal:
					if ord(
							letter) < 128:  # checking that the characters in the line are ASCII (ord(character)<128 for ASCII)
						element_list.append(letter)
					else:
						print "ERROR: Word contained non-ASCII character. It has been removed." # removes non-ASCII characters
				element = ''.join(element_list)
				line.append(element)

			file_as_list += [line, ]

		infile.close()

		return file_as_list


	@staticmethod
	def assigningEnum(variable_name, filedata, col1_id, col2_id):
		"""
		This function will assign the enum variable we've been reading the CSV to do.

		INPUT: <list> of <lists>
		RETURN: <tuple> of <tuples>
		"""

		print str(variable_name) + " = ("
		for row in filedata:
			print "\t(" + str(row[col1_id]) + ", '" + str(row[col2_id]).title() + "'),"
		print ")"
