from sm.settings import EV as EV
from su_tools import dataloader as dbr

if EV == 'HEROKU':
	dbr.collectstatic()