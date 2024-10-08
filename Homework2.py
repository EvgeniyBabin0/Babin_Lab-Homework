word = 'testing'  # Замените это слово на любое другое для проверки

# Определение длины слова
length = len(word)

# Проверка на четность или нечетность длины слова
if length % 2 == 1:
    # Если длина нечётная, выводим среднюю букву
    middle_index = length // 2
    middle_letter = word[middle_index]
    print(f"Результат: {middle_letter}")
else:
    # Если длина чётная, выводим две средних буквы
    middle_index1 = length // 2 - 1
    middle_index2 = length // 2
    middle_letters = word[middle_index1:middle_index2 + 1]
    print(f"Результат: {middle_letters}")