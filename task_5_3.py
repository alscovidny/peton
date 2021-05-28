tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_v1 = ['9А', '7В', '9Б', '9В', '8Б', '10А']
klasses_v2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '9В', '8Б', '10А']

klasses = klasses_v1

klasses.extend([None for j in range(len(tutors) - len(klasses))])
generated_tuples = ((tutors[i], klasses[i]) for i in range(len(tutors)))

print(f'Класс объекта "generated_tuples": {type(generated_tuples)}')
print(*generated_tuples)
print(next(generated_tuples))
