from datetime import date
from datetime import datetime


def getDays():
	curdate = datetime.today()
	f_date = date(2017, 10, 26)
	l_date = date(curdate.year, curdate.month, curdate.day)
	delta = l_date - f_date
	print(delta.days)
	return str(delta.days)