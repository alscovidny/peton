import re

pattern = re.compile(
		r'(?P<ip>.+) - - \[(?P<date>.*)\] \"(?P<req_type>[A-Z]+) (?=\/)(?P<req_res>/.*) HTTP.+\" (?P<res_code>[\d]+) (?P<res_size>[\d]+)'
		)


test_string = '80.91.33.133 - - [17/May/2015:08:05:14 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.16)"'

data_tuple = pattern.search(test_string).groups()

print(data_tuple)
