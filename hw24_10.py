import random
import string

def random_word(length=5):
   #  Генерирует случайное слово из букв английского алфавита
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def word_weight(word):
   #  Вычисляет вес слова как сумму значений его символов в Unicode
    return sum(ord(char) for char in word)

def binary_search(sorted_list, target_weight):
    # Бинарный поиск по весам слов в отсортированном списке
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_weight = list(sorted_list[mid].keys())[0]
        if mid_weight == target_weight:
            return mid
        elif mid_weight < target_weight:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Генерация списка случайных слов
word_list = [random_word(random.randint(3, 7)) for _ in range(10)]

# Преобразование слов в словари с весами
weighted_words = [{word_weight(word): word} for word in word_list]

# Сортировка списка по весам слов
weighted_words.sort(key=lambda x: list(x.keys())[0])

# Вывод отсортированного списка
print("Отсортированный список:", weighted_words)

# Ввод слова от пользователя
user_word = input("Введите слово для поиска: ")
user_weight = word_weight(user_word)

# Поиск слова
index = binary_search(weighted_words, user_weight)
if index != -1:
    print(f"Слово '{user_word}' найдено с весом {user_weight} на индексе {index}.")
else:
    print("Слово не найдено.")
