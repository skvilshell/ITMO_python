import helpers
from collections import Counter
import string
console = helpers.Console()


def work1(first_list: list, second_list:list) -> list:
   new_list = []
   for item1, item2 in zip(first_list, second_list):
      new_list.append(item1)  
      new_list.append(item2)
   return new_list

def work2(persons: list):
   filtered_persons = filter(lambda person: person[1] > 18, persons)
   sorted_persons = sorted(filtered_persons, key = lambda person: person[1], reverse=True)
   return sorted_persons

def work3(matrix: list):
   def minor_matrix(matrix, i, j):
      return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
   if len(matrix) == 1:
      return matrix[0][0]
   if len(matrix) == 2:
      return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
   det = 0
   for j in range(len(matrix)):
      det += ((-1) ** j) * matrix[0][j] * work3(minor_matrix(matrix, 0, j))
   return det

def work4(obj: object):
   return {value: key for key, value in obj.items()}

def work5(sets):
   if sets:
      return set.intersection(*sets)
   else:
      return set()
   
def work6(s: string):
   # Приводим текст к нижнему регистру
   s = s.lower()

   # Удаляем знаки препинания
   s = s.translate(str.maketrans('', '', string.punctuation))

   # Создаем список слов
   words = s.split()

   # Создаем словарь с подсчетом количества встречаемости слов
   word_count = Counter(words)

   # Сортируем словарь по убыванию количества встречаемости слов
   sorted_word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))

   console.okblue(sorted_word_count)



s = "Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде."
work6(s)