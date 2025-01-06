from functools import reduce


def work1(numbers: list):
   # Возведение чисел в третью степень с помощью функции map
   cubed_numbers = list(map(lambda x: x ** 3, numbers))

   # Отбор только четных чисел с помощью функции filter
   even_numbers = list(filter(lambda x: x % 2 == 0, cubed_numbers))

   # Нахождение произведения всех элементов списка с помощью функции reduce
   product = reduce(lambda x, y: x * y, even_numbers, 1)  # Начальное значение 1 для произведения

def is_prime(n:int):
   # Частный случай
   if n % 2 == 0:
        return n == 2
   d = 3
   while d * d <= n and n % d != 0:
      d += 2
   return d * d > n

def own_map(l: list, fn):
   return list(map(lambda x: fn(x)))

def work4(url: str):
   try:
      with open(url, 'r', encoding='utf-8') as file:
         lines = file.readlines()

      num_lines = len(lines)
      num_words = 0
      num_chars = 0
      longest_word = ""

      for line in lines:
         words = line.split()
         num_words += len(words)
         num_chars += len(line)

         for word in words:
               if len(word) > len(longest_word):
                  longest_word = word

      result = {
         'Строк': num_lines,
         'Слов': num_words,
         'Символов': num_chars,
         'Длинное слово': longest_word,
         'Символов в длинном слове': len(longest_word)
      }

      return result

   # обработка ошибок
   except FileNotFoundError:
      return {'error': 'File not found'}
   except Exception as e:
      return {'error': str(e)}
   
print(work4("a.txt"))

def merge_files(file_paths, write_to_file=True, output_filename='merged_output.txt'):
   try:
      merged_content = ""

      for file_path in file_paths:
         with open(file_path, 'r', encoding='utf-8') as file:
               merged_content += file.read() + '\n'

      if write_to_file:
         with open(output_filename, 'w', encoding='utf-8') as output_file:
               output_file.write(merged_content)

      return merged_content

   except FileNotFoundError:
      return 'One or more files not found'
   except Exception as e:
      return str(e)

def hash_table():
   # Функция создает хеш для строки, 
   # склеивая юникод-значения символов 
   # и возвращая остаток от деления 
   # для получения индекса
   def my_hash(string, table_size=256):
      unicode_str = ''.join(str(ord(char)) for char in string)
      return int(unicode_str) % table_size
   

   # функция добавляет строку в хеш-таблицу, 
   # обрабатывая случаи наличия строки в таблице
   def add_to_table(hash_table, string, table_size=256):
      index = my_hash(string, table_size)
      if index not in hash_table:
         hash_table[index] = []

      if string in hash_table[index]:
         print(f'Ошибка: Строка "{string}" содержится в таблице .')
      else:
         hash_table[index].append(string)
         print(f'Строка "{string}" добавлена.')
         return hash_table
   
   # функция удаляет строку из таблицы 
   # и обрабатывает случаи, когда строка отсутствует
   def remove_from_table(hash_table, string, table_size=256):
      index = my_hash(string, table_size)
      if index in hash_table and string in hash_table[index]:
         hash_table[index].remove(string)
         print(f'Строка "{string}" удалена из таблицы.')
      else:
         print(f'Предупреждение: Строка "{string}" не найдена в таблицы.')
      return hash_table
   
   # функция ищет строку в таблице и возвращает её индекс
   #  и позицию в списке или False, если строка не найдена
   def search_in_table(hash_table, string, table_size=256):
      index = my_hash(string, table_size)
      if index in hash_table and string in hash_table[index]:
         return index, hash_table[index].index(string)
      return False
   
   hash_table = {}
   # Тут работа с консолью. Выбор опций
   while True:
      print("\n1 - Добавить строку\n2 - Удалить строку\n3 - Найти строку\n4 - Показать таблицу\n5 - Выход")
      choice = input("Enter choice: ")

      if choice == '1':
            string = input("Ввести строку для добавления: ")
            hash_table = add_to_table(hash_table, string)
      elif choice == '2':
            string = input("Введите строку для удаления: ")
            hash_table = remove_from_table(hash_table, string)
      elif choice == '3':
            string = input("Введите строку для поиска: ")
            result = search_in_table(hash_table, string)
            if result:
               print(f'Строка найдена по индексу {result[0]} и позиции {result[1]}')
            else:
               print('Строка не найдена')
      elif choice == '4':
            print(hash_table)
      elif choice == '5':
            break
      else:
            print("Не валидный ввод. Повторите.")