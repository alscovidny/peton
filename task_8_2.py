import re

pattern = re.compile(
		r'(?P<ip>.+) - - \[(?P<date>.*)\] \"(?P<req_type>[A-Z]+) (?=\/)(?P<req_res>/.*) HTTP.+\" (?P<res_code>[\d]+) (?P<res_size>[\d]+)'
		)

test_string = '80.91.33.133 - - [17/May/2015:08:05:14 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.16)"'

def parse_test_string():
	parsed_row = pattern.search(test_string).groups()
	print(parsed_row)

def parse_from_nginx():
	with open("nginx_logs.txt", encoding = 'utf-8') as f:

		for line in f:
			parsed_row = pattern.search(line).groups()
			print(parsed_row)

parse_test_string()
# parse_from_nginx()