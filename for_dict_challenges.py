# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
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

student_names = [name['first_name'] for name in students]
unique_names = set(student_names)
for name in unique_names:
    print(f'{name}: {student_names.count(name)}')
print()


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
student_names = [name['first_name'] for name in students]  
print(f'Самое частое имя среди учеников: {Counter(student_names).most_common(1)[0][0]}')
print()


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
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
class_number = 0
for students in school_students:
    class_number += 1
    names = [name['first_name'] for name in students]
    count_names = {name: names.count(name) for name in names}
    max_value = max(count_names, key=count_names.get) 
    print(f'Самое частое имя в классе {class_number}: {max_value}')

print()
    
    
    


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for classes in school:
    cmale, cfemale = 0, 0
    for name in classes['students']:
        if is_male.get(name['first_name']):
            cmale += 1
        else:
            cfemale += 1
    print(f'Класс {classes['class']}: девочки {cfemale}, мальчики {cmale}')

    print()


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
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

male = []
female = []
for grade in range(len(school)):
    male.append(0)
    female.append(0)
    for student in school[grade]['students']:
        if is_male[student['first_name']]:
            male[grade] += 1
        else:
            female[grade] += 1

most_male_index = male.index(max(male))
most_male_class = school[most_male_index]['class']
most_female_index = female.index(max(female))
most_female_class = school[most_female_index]['class']
print(f"Больше всего мальчиков в классе {most_male_class}")
print(f"Больше всего девочек в классе {most_female_class}")
