# Вывести последнюю букву в слове
from itertools import count


word = 'Архангельск'
print(word[-1])
# +

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))
# # +

# Вывести количество гласных букв в слове
word = 'Архангельск'
leters_1 = ['а', 'е']
summ=0
for leter in leters_1:
    let_2 = (word.lower().count(leter))
    summ=summ+let_2
print(summ)
# заморочено слишком, но вроде бы решил, позже попробую упростить!

# # Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
# +

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
first_leter = sentence.split(' ') # [приводим к списку]
for leter in first_leter:
    print(leter[0])
# +

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sred_1 = sentence.split()  # [приводим к списку]
summ =0
for word in sred_1:
    summ = summ+len(word)
    sred=summ/len(sred_1)
print(sred)
# +
