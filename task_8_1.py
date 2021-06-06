import re

def parse_email(email):

	info = re.compile(r"(?P<username>.*)@(?P<domain>.+\..+)")

	try:
		parsed_dict = info.match(email).groupdict()
	except AttributeError:
		msg = f'wrong e-mail: {email}'
		raise ValueError (msg)

	return parsed_dict

print(parse_email(str(input('введите e-mail: '))))
