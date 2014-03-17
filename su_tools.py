__author__ = 'Ammar Akhtar'

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sm.settings")

#__author__ = 'aakh'
from getpass import getpass
from datetime import datetime
from inspect import stack
from django.core import management
from defaultdata import DatabaseReload as dd
from smcore.utilities import validations

now = datetime.now


class dataloader():
	"""Power tools for admins. type .listmethods() for contents"""

	# locations.Addresses.create(building='9', street_name='Appold Street', postcode='EC2A2AP')

	@staticmethod
	def full_reload():
		print "\n", now(), stack()[0][3]
		#dataloader.generate_users()
		#dd.generate_banking_companies()
		dd.full_reload()
		# dd.generate_countries()
		print now(), stack()[0][3], " finished\n"


	@staticmethod
	def manage_flush(u_pw=None):
		print "\n", now(), stack()[0][3]
		pw = "letmein"
		print 'This will irreversibly delete the data base.'

		if validations.is_empty_or_false(u_pw):
			u_pw = getpass()

		if u_pw == pw:
			management.call_command('flush', interactive=False)
			print "flush completed"

		else:
			print "invalid password, exitting"
		print now(), stack()[0][3], " finished\n"

	@staticmethod
	def manage_syncdb():
		management.call_command('syncdb', interactive=False)
		dataloader.manage_migrate()

	@staticmethod
	def collectstatic():
		management.call_command('collectstatic', interactive=False)

	@staticmethod
	def manage_schemamigration(mig_type=None, auto=True, app='smcore'):
		if mig_type == 'initial':
			#dataloader.manage_syncdb()
			print "schemamigration initial"
			management.call_command("schemamigration", app, initial=True, verbosity=1)
		else:
			print "schemamigration auto"
			management.call_command("schemamigration", app, auto=True, verbosity=1)

		dataloader.manage_migrate(app=app, fake='fake')

	@staticmethod
	def manage_convert_to_south(app='smcore'):
		management.call_command("convert_to_south", app=app, verbosity=1)

	@staticmethod
	def manage_migrate(app=None, fake=False):
		if validations.is_empty_or_false(app):
			print "python manage.py migrate"
			management.call_command("migrate", verbosity=1)

		elif fake == 'fake':
			print "python manage.py migrate fake"
			management.call_command("migrate", fake=True, verbosity=1)

		else:
			print "python manage.py migrate " + str(app)
			management.call_command("migrate", app, verbosity=1)


	@staticmethod
	def manage_dumpdata(u_path=None):
		print "\n", now(), stack()[0][3]
		# print u_path

		if validations.is_empty_or_false(u_path):
			# if a path is not provided
			# dump to the below path with appropriate timestamp
			u_path = 'db/extract' + now().strftime("%Y%m%d%H%M%S%f") + '.json'

		#print u_path
		output = open(u_path, 'w')
		management.call_command('dumpdata', fmt='json', indent=4, stdout=output)   # use_natural_keys=True
		output.close()
		print now(), stack()[0][3], " finished to ./%s\n" % u_path


	@staticmethod
	def manage_loaddata(u_path=None):
		print "\n", now(), stack()[0][3]
		# print u_path

		if validations.is_empty_or_false(u_path):
			u_path = raw_input('enter the path to file eg: "dir/file.ext"')

		management.call_command('loaddata', u_path, verbosity=1)
		print now(), stack()[0][3], " finished\n"


	@classmethod
	def listmethods(cls):
		for m in dir(cls): print m

	#print zip*(self.__dict__)[0]

	@classmethod
	def help(cls):
		return cls.__doc__, cls.listmethods()
