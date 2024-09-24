from datetime import datetime
import helpers



console = helpers.Console()


def work1():

   console.new_work(1)

   print("Введите значение для x и y")
   x,y = input("X:"),input("Y:")

   # Проверка что пользователь ввел число
   while not (x.isdigit() and y.isdigit()):

      if not (x.isdigit() or y.isdigit()):
         print("Вы не ввели цифры для x и y")
         x,y = input("X:"),input("Y:")
      elif not x.isdigit():
         print("Вы не ввели X")
         x = input("X:")
      elif not y.isdigit():
         print("Вы не ввели y")
         y = input("Y:")

   x = int(x)
   y = int(y)

   print(f"x + y = {x + y}")
   print(f"x - y = {x - y}")
   print(f"x * y = {x * y}")
   if y == 0:
      print("На 0 делить нельзя")
   else:
      print(f"x / y = {x / y}")
      print(f"Остаток от деления: {x % y}")
   print(f"x^y: {x ** y}")

def work2():
   console.new_work(2)

   s = input("Введите строку:")
   l = len(s)
   s_second: str = ""
   s_new: str = ""

   for i in range(l):
      if( i % 2 == 0):
         s_second = s_second + s[i]
      s_new = s_new + s[l - (i + 1)]
   
   print(s_second)
   print(s_new)

def work3():
   console.new_work(3)
   # ввод числа
   last_index = helpers.input_number()
   list_sum = 0
   s_second = ""
   new_list = []

   while last_index != -1:
      new_list.append(last_index)
      type(last_index)
      list_sum += last_index
      if last_index % 2 == 0:
         s_second += f"{last_index}"
      last_index = helpers.input_number()
   
   print(f"длинна: {len(new_list)}")
   print(f"сумма: {list_sum}")
   print(f"четные:{s_second}")

   return new_list

def work4():
   console.new_work(4)
   
   new_list = work3()
   length = len(new_list)

   for i in range(length):
      if( ( new_list[i] % 3 == 0) or (new_list[i] % 5 == 0) and (new_list[i] % 15 != 0) ):
         print(new_list[i])
   
   print(f"Последний элемент: {new_list[length-1]}")


def work5():
   console.okcyan("Введите день")
   d = helpers.input_number()
   console.okcyan("Введите месяц")
   m = helpers.input_number()
   console.okcyan("Введите число")
   y = helpers.input_number()

   # Определение квартала
   if 1 <= m <= 3:
      print("первый квартал")
   elif 4 <= m <= 6:
      print("второй квартал")
   elif 7 <= m <= 9:
      print("третий квартал")
   elif 10 <= m <= 12:
      print("четвертый квартал")
   else:
      print("Неверный месяц")

   # високосный
   if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
      print("Високосный")
   else:
      print("Не високосный")
   
   
   current_date = datetime.now()
   birth_date = datetime(y, m, d)
   
   # Рассчитываем количество дней с момента рождения
   days_passed = (current_date - birth_date).days
   
   # Возвращаем количество лет с учетом средней длины года в 365.25 дней
   print(days_passed + (days_passed / 365.25))


work1()
work2()
work3()
work4()
work5()