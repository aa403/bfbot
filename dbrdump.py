__author__ = 'Ammar Akhtar'

import sys
from su_tools import dataloader as dbr

# print sys.argv

try:
	dbr.manage_dumpdata(sys.argv[1])
except:
	dbr.manage_dumpdata()

############

