# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from re import A


students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
for student in students:
    print(student)
# for k, v in students.items:
#     print(f"{k}>>>{v}")
# for student in students:
#     stud_1 = students[0]
#     # print(stud_1)
#     print(f'{stud_1} {stud_1.count(students[0])}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# for student in students:
#     common_name = students.count(student)
#     name_student = (student['first_name'])
#     print(f'Самое частое имя среди учеников: {common_name}')
    # print(f'Самое частое имя среди учеников: {students.count(student)}')
# ???


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
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???


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
# ???

# # пример из лекции
# # нужно вывести среднюю оценку по каждому классу и по всей школе
# classes = [
#     {'name': '3А', 'scores': [3,4,4,5,2]},
#     {'name': '3Б', 'scores': [5,5,3,2,2]},
#     {'name': '3В', 'scores': [4,5,3,5,4]},
# ]
# def count_average(students_scores):
#     scores_sum = 0
#     for score in students_scores:
#         scores_sum += score
#     scores_avg = scores_sum / len(students_scores)
#     return scores_avg
# for one_class in classes:
#     class_score_avg = count_average(one_class['scores'])
#     print(f"Средняя оценка для класса {one_class['name']}: {class_score_avg}")


# тренировка по словарям
# dict_sample = {"Company": "Toyota", "model": "Premio", "year": "2012"}
# dict_sample["Country"] = "Japan"
# dict_sample["Color"] = "Red"
# dict_sample["Company"] = "Honda"
# del dict_sample["year"]
# dict_sample["year"] = "2015"
# x = dict_sample.items()
# print(x)
# dict_sample["year"] = "2019"
# print(x)
# # dict_sample.clear()



# dict = {'Name': 'Mercy', 'Age': 23, 'Course': 'Accounting'}
#     #   {'Name': 'Nik', 'Age': 30, 'Course': 'PHP'}
#     #   {'Name': 'Alex', 'Age': 40, 'Course': 'Python'}


# print("Student Name:", dict['Name']) 
# print("Course:", dict['Course']) 
# print("Age:", dict['Age'])

# prices = [29.30, 10.20, 44.00, 5.99, 81.90]
# for index, item in enumerate(prices):
# 	if item > 40:
# 		prices[index] = round(prices[index] - (prices[index] * 30 / 100), 2)

# print(prices)

# тренировка на словари

# Capitals = dict()
# Capitals['Russia'] = 'Moscow'
# Capitals['Ukrain'] = 'Kiev'
# Capitals['USA'] = 'Washington'

# Countries = ['Russia', 'France', 'USA', 'Russia']

# for country in Countries:
#     # Для каждой страны из списка проверим, есть ли она в словаре Capitals
#     if country in Capitals:
#         print('Столица страны ' + country + ': ' + Capitals[country])
#     else:
#         print('В базе нет страны с названием - ' + country)

# Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
# Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
# Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
# Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
# print(Capitals)
