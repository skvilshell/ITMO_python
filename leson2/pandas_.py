import seaborn as sns
import pandas as pd

# Загрузка датасета "Titanic"
titanic = sns.load_dataset('titanic')

# Вывод первых нескольких строк датасета
print(titanic.describe())
# Индексация по меткам
print(titanic['survived'])  # Один столбец
print(titanic[['survived', 'age']])  # Несколько столбцов

# Индексация по позиции
print(titanic.iloc[0])  # Первая строка
print(titanic.iloc[:, 1])  # Второй столбец
print(titanic.iloc[0:2, 1:3])  # Подмассив

# Фильтрация данных
adults = titanic[titanic['age'] > 18]
print(adults)