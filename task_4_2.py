from decimal import Decimal
from datetime import date
import requests

# with open('XML_daily.asp','rt',encoding = 'cp1251') as f:
# 	lines_str = f.readline().split('<Valute ID')

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
lines_str = str(response.content).split('<Valute ID')

def currency_rates(currency,type_data = 'float'):

	type_data = type_data.lower()

	day, month, year = lines_str[0][ lines_str[0].find('Date="') + len('Datr="') : lines_str[0].find('" name') ].split('.')

	for line in lines_str[1:]:
		
		find_currency = '<CharCode>' + currency.upper() + '</CharCode>'
		idx = line.find(find_currency)

		nominal = int(line[line.find("<Nominal>") + len('<Nominal>') : line.find('</Nominal>')])

		if idx > 0:
			idx_first = line.find('<Value>', idx)
			idx_last = line.find('</Value>', idx_first)
			
			if type_data == 'float':
				return float(line[idx_first + len('<Value>') : idx_last].replace(',','.')) / nominal, \
					   date(int(year), int(month), int(day))

			if type_data == 'decimal':
				return Decimal(line[idx_first + len('<Value>') : idx_last].replace(',','.')) / nominal, \
					   date(int(year), int(month), int(day))
	return None	

print(currency_rates('usd'))
