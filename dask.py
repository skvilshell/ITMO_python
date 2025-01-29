import os
import zipfile
import dask.dataframe as dd
from sqlalchemy import create_engine

# Разархивируем архив
archive_name = "recipes_full.zip"
unzip_dir = "recipes_full"

with zipfile.ZipFile(archive_name, 'r') as archive:
    archive.extractall(unzip_dir)

# Считываем все файлы из архива
files = [os.path.join(unzip_dir, f) for f in os.listdir(unzip_dir)]
data = dd.read_csv(files)

# Выводим метаинформацию о таблице
print("Количество партиций:", data.npartitions)
print("Типы данных столбцов:\n", data.dtypes)

# Выводим первые 5 строк
print("Первые 5 строк таблицы:")
print(data.head())

# Выводим последние 5 строк
print("Последние 5 строк таблицы:")
print(data.tail())

# Подсчитываем количество строк в каждом блоке
block_sizes = data.map_partitions(len).compute()
print("Количество строк в каждом блоке:", block_sizes.tolist())

# Находим максимум в столбце n_steps и визуализируем граф вычислений
import dask
from dask.diagnostics import visualize

max_steps = data['n_steps'].max()
dask.visualize(max_steps, filename='max_steps_graph')
print("Максимальное количество шагов в рецептах:", max_steps.compute())

# Количество отзывов по месяцам
data['review_date'] = dd.to_datetime(data['review_date'])
data['review_month'] = data['review_date'].dt.to_period('M')
reviews_by_month = data.groupby('review_month').size().compute()
print("Количество отзывов по месяцам:\n", reviews_by_month)

# Находим пользователя, который отправил больше всего рецептов
top_user = data['submitted_by'].value_counts().idxmax().compute()
print("Пользователь, отправивший больше всего рецептов:", top_user)

# Находим самый первый и самый последний рецепт
first_recipe = data.loc[data['submitted_date'].idxmin()].compute()
last_recipe = data.loc[data['submitted_date'].idxmax()].compute()
print("Самый первый рецепт:\n", first_recipe)
print("Самый последний рецепт:\n", last_recipe)

# Загружаем данные в SQLite
engine = create_engine('sqlite:///recipes.db')
data.to_sql('recipes', engine, if_exists='replace', index=False)

# Фильтрация по медианному времени приготовления и среднему количеству шагов
median_prep_time = data['prep_time'].median().compute()
mean_steps = data['n_steps'].mean().compute()
filtered_recipes = data[(data['prep_time'] < median_prep_time) & (data['n_steps'] < mean_steps)]
filtered_recipes.compute().to_csv('filtered_recipes.csv', index=False)

print("Отфильтрованные рецепты сохранены в filtered_recipes.csv")