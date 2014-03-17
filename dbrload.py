__author__ = 'Ammar Akhtar'
import sys
from su_tools import dataloader as dbr
#print sys.argv
#dbr.manage_schemamigration('auto') #manage.py schemamigration sm --auto
#dbr.manage_migrate()
if len(sys.argv) > 1:
	if sys.argv[1] in ['f', 'flush']:
		dbr.manage_flush()
	elif sys.argv[1] in ['r', 'reload']:
		dbr.manage_loaddata(sys.argv[2])
	elif sys.argv[1] in ['d', 'default']:
		dbr.full_reload()
else:
	print "This command does a database load. Please provide a type:"
	print "'r path/to/file.json' or 'reload path/to/file.json' to load from file"
	print "'d' or 'default' to load from system default"
	print "'f' or 'flush' to flush"

############

