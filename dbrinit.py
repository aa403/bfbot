__author__ = 'Ammar Akhtar'

import os
from sm.settings import BASE_DIR as BASE_DIR
#from sm.settings import EV as EV
from su_tools import dataloader as dbr

path_to_initialdotpy = os.path.join(BASE_DIR, 'smcore', 'migrations', '0001_initial.py')
print path_to_initialdotpy

dbr.manage_syncdb()

if os.path.isfile(path_to_initialdotpy):
	print 'Initial migration file already exists in %s' % path_to_initialdotpy
	print 'No need to execute initial migration command'

else:
	print "building initial migration"
	dbr.manage_schemamigration(mig_type='initial', app='smcore') #manage.py schemamigration smcore --initial
