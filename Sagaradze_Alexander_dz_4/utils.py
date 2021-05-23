from decimal import Decimal
import datetime
import requests

def currency_rates(currency,type_data = 'float'):

	response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
	lines_str = str(response.content).split('<Valute ID')

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
					   datetime.date(int(year), int(month), int(day)).strftime('%Y-%m-%d')

			if type_data == 'decimal':
				return Decimal(line[idx_first + len('<Value>') : idx_last].replace(',','.')) / nominal, \
					   datetime.date(int(year), int(month), int(day)).strftime('%Y-%m-%d')
	return None