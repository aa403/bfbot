__author__ = 'Ammar Akhtar'
import sys
from su_tools import dataloader as dbr

try:
	if sys.argv[1] in ['i', 'initial']:
		dbr.manage_schemamigration('initial') #manage.py schemamigration sm --auto


except:
	print "manage_schemamigration auto"
	dbr.manage_schemamigration('auto') #manage.py schemamigration sm --auto
