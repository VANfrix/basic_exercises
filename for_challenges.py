# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
len_0 =len(names[0])
print(f'{names[0]}: {len_0}')
len_1 =len(names[1])
print(f'{names[1]}: {len_1}')
len_2 =len(names[2])
print(f'{names[2]}: {len_2}')
len_3 =len(names[3])
print(f'{names[3]}: {len_3}')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}


names = ['Оля', 'Петя', 'Вася', 'Маша']


print(is_male['Оля'])


print(names[0])
print(names[1])
print(names[2])
print(names[3])
# # ???


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
len_1 =len(groups)
print(f'Всего {len_1} группы.')
len_0_groupe = len(groups[0])
print(f'Группа 1: {len_0_groupe} ученика.')
len_1_groupe = len(groups[1])
print(f'Группа 2: {len_1_groupe} ученика')
# ???


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
print(f'Группа 1: {groups[0]}')
print(f'Группа 1: {groups[1]}')
# ???