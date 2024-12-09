# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэ'
vcounter = 0
for c in word:
    if c.lower() in vowels:
        vcounter += 1
print(vcounter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
splitsent = sentence.split()
for i in splitsent:
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
splitsent = sentence.split()
sumlen = 0
for word in splitsent:
    sumlen += len(word)
print(sumlen / len(splitsent))