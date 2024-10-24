def work1():
   # Возведение чисел в третью степень с помощью функции map
   cubed_numbers = list(map(lambda x: x ** 3, numbers))

   # Отбор только четных чисел с помощью функции filter
   even_numbers = list(filter(lambda x: x % 2 == 0, cubed_numbers))

   # Нахождение произведения всех элементов списка с помощью функции reduce
   product = reduce(lambda x, y: x * y, even_numbers, 1)  # Начальное значение 1 для произведения