__author__ = 'Ammar Akhtar'

import sys
from su_tools import dataloader as dbr

#print sys.argv

print
print "Note that an input of 'fake' will be used to execute 'migrate --fake'"

try:
	if sys.argv[1] == 'fake':
		dbr.manage_migrate(fake=sys.argv[1])
	else:
		dbr.manage_migrate(sys.argv[1])
except:
	dbr.manage_migrate()


