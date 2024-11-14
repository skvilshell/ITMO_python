import numpy as np

# Одномерный массив
arr1 = np.array([1,4,5])

# Двумерный массив (матрица)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Массив с нулями
zeros = np.zeros((3, 4))

# Массив с единицами
ones = np.ones((2, 3))

# Массив с случайными числами
random = np.random.random((2, 2))

# print(arr1)
# print(arr2)
# print(zeros)
# print(ones)
# print(random)

# # Размерность массива
# print(arr2.shape)

# # Количество измерений
# print(arr2.ndim)

# # Общее количество элементов
# print(arr2.size)

# # Тип данных элементов
# print(arr2.dtype)

# # Индексация
# print(arr1[0])  # Первый элемент
# print(arr2[1, 2])  # Элемент в строке 1, столбце 2

# # Срезы
# print(arr1[1:10])  # Элементы с 1 по 2
# print(arr2[:, 1])  # Все строки, второй столбец

# # Сумма элементов
# print(np.sum(arr1))

# # Среднее значение
# print(np.mean(arr1))

# # Стандартное отклонение
# print(np.std(arr1))

# # Максимум и минимум
# print(np.max(arr1))
# print(np.min(arr1))

# print(arr2.sum(axis = 0))

# l = [[1, 2], [3, 4]]

# m = np.matrix(l)

# print(m.sum(axis = 0))


# Сохранение массива в файл
np.save('array.npy', arr1)

# Загрузка массива из файла
loaded_array = np.load('array.npy')
print(loaded_array)
