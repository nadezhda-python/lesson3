# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

names_dict = {}

for student in students:
  names_dict.setdefault(student['first_name'], 0)
  names_dict[student['first_name']] += 1

for name in names_dict:
  print (f'{name} {names_dict[name]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

names_dict = {}
max_amount, max_name = 0, ''

for student in students:
  names_dict.setdefault(student['first_name'], 0)
  names_dict[student['first_name']] += 1
  if names_dict[student['first_name']] > max_amount:
    max_amount = names_dict[student['first_name']]
    max_name = student['first_name']

print (f'Самое частое имя среди учеников: {max_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for idx, class_ in enumerate(school_students):
  class_number =  idx + 1
  class_names_dict = {}
  most_popular_name = ''
  max_name_frequency = 0
  for student in class_:
    class_names_dict.setdefault(student['first_name'], 0)
    class_names_dict[student['first_name']] += 1
    if class_names_dict[student['first_name']] > max_name_frequency:
      max_name_frequency = class_names_dict[student['first_name']]
      most_popular_name = student['first_name']
  print (f'Самое частое имя в классе {class_number}: {most_popular_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_ in school:
  male_amount = 0
  female_amount = 0
  for student in class_['students']:
    if is_male[student['first_name']]: 
      male_amount += 1
    else:
      female_amount += 1
  print (f'В классе {class_["class"]} {female_amount} девочки и {male_amount} мальчика.')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]

is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

max_female_amount = 0
max_female_class = ''
max_male_amount = 0
max_male_class = ''

for class_ in school:
  male_amount = 0
  female_amount = 0

  for student in class_['students']:
    if is_male[student['first_name']]: 
      male_amount += 1
    else:
      female_amount += 1

  if max_female_amount < female_amount:
    max_female_amount = female_amount
    max_female_class = class_["class"]
  
  if max_male_amount < male_amount:
    max_male_amount = male_amount
    max_male_class = class_["class"]

print(f'Больше всего мальчиков в классе {max_male_class}')
print(f'Больше всего девочек в классе {max_female_class}')

