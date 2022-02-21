# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
# word = 'Архангельск'
# leter = word.len()
# print(leter)
# тупик!!!

# Вывести количество гласных букв в слове
# word = 'Архангельск'
# print(len(word()


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for leter in sentence:
    print(leter.lower())


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sred_1 = (sentence.split())
sred_2 = (len(sred_1[0]) +len(sred_1[1]) +len(sred_1[2]) +len(sred_1[3]))/len(sred_1)
# print(sred_1)
print(int(sred_2))