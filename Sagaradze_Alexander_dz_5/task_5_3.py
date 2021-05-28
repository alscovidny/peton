tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_v1 = ['9А', '7В', '9Б', '9В', '8Б', '10А']
klasses_v2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '9Б', '9В', '8Б', '10А']

def make_tuples(klasses, tutors):

	klasses = klasses.copy()
	klasses.extend([None for j in range(len(tutors) - len(klasses))])
	return ((tutors[i], klasses[i]) for i in range(len(tutors)))

print(type(make_tuples(klasses_v1,tutors)))

tuples_1 = make_tuples(klasses_v1,tutors)
print(*tuples_1, '\n')

tuples_2 = make_tuples(klasses_v2,tutors)
print(*tuples_2)
print(next(tuples_2))
