def num_translate_adv(content):
    
    translate_dict = {
				   'zero': 'нуль','one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
				   'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten' : 'десять',
				   'Zero': 'Нуль','One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
				   'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten' : 'Десять',
    }

    print(translate_dict.get(content))

#ввод для автоматизированного тестирования
num_translate_adv((input("input numeral from 0 to 10: ")))
