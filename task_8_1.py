import re

def parse_email(email):

	name = re.compile(r"(?P<username>.*(?=@))")

	domain = re.compile(r"(?P<domain>(?<=@).+\..+)")

	# name = re.compile(r'.*(?=@)', re.IGNORECASE)
	# domain = re.compile(r'(?<=@).+\..+', re.IGNORECASE)

	parced_name = name.match(email).group()

	if not domain.search(email):
		raise ValueError (f'wrong e-mail: {email}')
	
	else:
		parced_domain = domain.search(email).group()

	return parced_name, parced_domain

print(parse_email('yandex@mail.com'))
