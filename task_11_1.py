import re
import sys

class Date:

	def __init__(self, date = ''):
		self.date = date

	def __str__(self):
		return self.date

	@staticmethod
	def validate(date_param):
		try:
			pattern = re.compile(r'^(?P<day>\d+)-(?P<month>\d+)-(?P<year>\d+)$')
			day, month, year = map(lambda x : int(x), re.search(pattern, date_param).groups())
			if day not in range(1,32):
				print(f'incorrect day: {day}')
				sys.exit(1)
			if month not in range(1,13):
				print(f'incorrect month: {month}')
				sys.exit(2)
		except AttributeError:
			print('incorrect date')
			sys.exit(3)
		return day, month, year

	@classmethod
	def parse_date(cls, date_param):
		return Date.validate(date_param)


birthday = Date()
print(birthday.parse_date('17-8-2019'))

date = Date()
print(date.validate('02-13-1998'))
