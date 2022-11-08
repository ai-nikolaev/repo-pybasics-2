tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]
result = [(x[1], dict(enumerate(groups)).get(x[0], None))
          for x in enumerate(tutors)]
print(f'Ученики: {tutors}')
print(f'Классы: {groups}')
print(f'Список: {result}')
