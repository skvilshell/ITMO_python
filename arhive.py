import os
import pandas as pd
import numpy as np
import zipfile
from sqlalchemy import create_engine

# Разархивируем
archive_name = "recipes_full.zip"
unzip_dir = "recipes_full"

with zipfile.ZipFile(archive_name, 'r') as archive:
   archive.extractall(unzip_dir)

# 1 файл читает
first_file = os.listdir(unzip_dir)[0]
file_path = os.path.join(unzip_dir, first_file)
data = pd.read_csv(file_path)

# вывод типов
data_types = data.dtypes
print("Data Types:\n", data_types)

# Поиск максимального в n_steps
max_steps = data['n_steps'].max()
print("Maximum number of steps:", max_steps)

# Подсчет review с группировкой по month
data['review_date'] = pd.to_datetime(data['review_date'])
data['review_month'] = data['review_date'].dt.to_period('M')
reviews_by_month = data.groupby('review_month').size()
print("Отзывы сгруппированы по месяцам:\n", reviews_by_month)

# Поиск пользователя с наибольшим количеством отправленных рецептов
top_user = data['submitted_by'].value_counts().idxmax()
print("Пользователи с наибольшим количеством заявок:", top_user)

# ищем первый и последний отправленные рецепты
first_recipe = data.loc[data['submitted_date'].idxmin()]
last_recipe = data.loc[data['submitted_date'].idxmax()]
print("Представлен первый рецепт:\n", first_recipe)
print("Последний отправленный рецепт:\n", last_recipe)

# Рассчитывается медианные значения ингредиентов и времени приготовления
median_ingredients = data['n_ingredients'].median()
median_prep_time = data['prep_time'].median()
print("Среднее количество ингредиентов:", median_ingredients)
print("Среднее время подготовки:", median_prep_time)

# Поиск простого рецепта
simplest_recipe = data.loc[
    data.sort_values(by=['n_ingredients', 'prep_time', 'n_steps']).index[0]
]
print("Самый простой рецепт:\n", simplest_recipe)

# загрузка
db_engine = create_engine('sqlite:///recipes.db')
data.to_sql('recipes', db_engine, if_exists='replace', index=False)

# Фильтровать рецепты, у которых время приготовления меньше среднего и количество шагов меньше среднего.
mean_steps = data['n_steps'].mean()
filtered_recipes = data[(data['prep_time'] < median_prep_time) & (data['n_steps'] < mean_steps)]
filtered_recipes.to_csv('filtered_recipes.csv', index=False)

print("Отфильтрованные рецепты сохранены в filtered_recipes.csv")