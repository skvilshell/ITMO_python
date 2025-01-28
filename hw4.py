import random
import re
import string
import requests
import numpy as np

def hw4_1(url: str):
   email_re = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
   phone_re = r'(?:\+\d{1,3}\s?)?(?:\(?\d{1,4}\)?[\s.-]?)?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,9}'

   with open(url, 'r', encoding = 'utf-8') as f:
      s = f.read()

   phone_result = re.findall(phone_re, s)
   email_result = re.findall(email_re, s)

   with open('result.txt', 'w', encoding='utf-8') as f:
      f.write(phone_result.__str__())
      f.write(email_result.__str__())

# hw4_1('e.txt')

def hw4_2(username: str):
   res = requests.get(f"https://api.github.com/users/{username}").json()
   
   print(res['name'])
   print(res['public_repos'])

# hw4_2('skvilshell')

def hw4_3():
   # Генерация случайной квадратной матрицы 10x10
   matrix_a = np.random.rand(10, 10)
   print("Матрица A:")
   print(matrix_a)

   # Вычисление определителя
   determinant = np.linalg.det(matrix_a)
   if np.isclose(determinant, 0):
      print("Матрица A вырождена (определитель равен нулю).")
   else:
      print(f"Определитель матрицы A: {determinant}")

   # Транспонирование матрицы
   transposed_a = matrix_a.T
   print("Транспонированная матрица А:")
   print(transposed_a)

   # Ранг матрицы
   rank = np.linalg.matrix_rank(matrix_a)
   print(f"Ранг матрицы A: {rank}")

   # Собственные значения и собственные векторы
   eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
   print("Собственные значения матрицы А:")
   print(eigenvalues)
   print("Собственные векторы матрицы A:")
   print(eigenvectors)

   # Генерация второй матрицы 10x10
   matrix_b = np.random.rand(10, 10)
   print("Матрица B:")
   print(matrix_b)

   # Сложение матриц
   sum_matrix = matrix_a + matrix_b
   print("Сумма матриц:")
   print(sum_matrix)

   # Умножение матриц
   product_matrix = np.dot(matrix_a, matrix_b)
   print("Умножение матриц")
   print(product_matrix)

# hw4_3()

def hw4_5(length):
   characters = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(random.choice(characters) for _ in range(length))
   print(password)

# hw4_5(10)

import os
import shutil
import time
from datetime import datetime
import threading



def hw4_6():

   def backup_data(source_dir, target_dir, interval):
      try:
         while True:
            # Создание папки с датой и временем
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_dir = os.path.join(target_dir, timestamp)
            os.makedirs(backup_dir, exist_ok=True)

            # Копирование файлов и папок
            shutil.copytree(source_dir, backup_dir, dirs_exist_ok=True)

            print(f"Резервная копия создана в: {backup_dir}")

            # Ожидание перед следующей резервной копией
            time.sleep(interval)
      except KeyboardInterrupt:
         print("\nПроцесс резервного копирования прерван. Выход...")
      except Exception as e:
         print(f"Error: {e}")

   # Запрос данных у пользователя
   source_dir = input("Введите исходный каталог для резервного копирования: ").strip()
   target_dir = input("Введите целевой каталог для резервных копий:").strip()

   if not os.path.isdir(source_dir):
      print("Не существует такого каталога")
      return

   if not os.path.isdir(target_dir):
      print("Создается каталог")
      os.makedirs(target_dir, exist_ok=True)

   try:
      interval = int(input("Введите интервал резервного копирования в секундах:").strip())
      if interval <= 0:
         print("Интервал должен быть положительным числом. Выход")
         return
   except ValueError:
      print("Неверный интервал. Пожалуйста, введите номер. Выход")
      return

   print("Запуск процесса резервного копирования. Нажмите Ctrl+C, чтобы остановить")

   # Запуск резервного копирования в отдельном потоке
   backup_thread = threading.Thread(target=backup_data, args=(source_dir, target_dir, interval))
   backup_thread.daemon = True
   backup_thread.start()

   try:
      while True:
         command = input("Введите «exit», чтобы остановить процесс резервного копирования:").strip().lower()
         if command == 'exit':
               print("Остановка процесса")
               break
   except KeyboardInterrupt:
      print("\nПроцесс резервного копирования прерван. Выход...")

# hw4_6()