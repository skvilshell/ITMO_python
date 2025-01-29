import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
x_path = "x.csv"
y_path = "y.csv"

X = pd.read_csv(x_path, header=None)  # Признаки
y = pd.read_csv(y_path, header=None).values.ravel()  # Целевая переменная

# Разделение на тренировочную и тестовую выборки (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Проверим размеры выборок
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Функция для оценки модели
def evaluate_model(model, X_train, X_test, y_train, y_test):
   y_train_pred = model.predict(X_train)
   y_test_pred = model.predict(X_test)
   
   metrics = {
      "MSE_train": mean_squared_error(y_train, y_train_pred),
      "MSE_test": mean_squared_error(y_test, y_test_pred),
      "R2_train": r2_score(y_train, y_train_pred),
      "R2_test": r2_score(y_test, y_test_pred)
   }
   return metrics

# Словарь для хранения результатов
results = {}

# Линейная регрессия по каждому признаку отдельно
for i in range(X.shape[1]):
   model = LinearRegression()
   model.fit(X_train[[i]], y_train)
   results[f"Linear_X{i+1}"] = evaluate_model(model, X_train[[i]], X_test[[i]], y_train, y_test)

# Множественная линейная регрессия (по всем признакам)
multi_model = LinearRegression()
multi_model.fit(X_train, y_train)
results["Linear_Multi"] = evaluate_model(multi_model, X_train, X_test, y_train, y_test)

print(results)

# Полиномиальная регрессия степени 2 и 3 для каждого признака
degrees = [2, 3]

for degree in degrees:
   for i in range(X.shape[1]):
      poly = PolynomialFeatures(degree)
      X_train_poly = poly.fit_transform(X_train[[i]])
      X_test_poly = poly.transform(X_test[[i]])
      
      model = LinearRegression()
      model.fit(X_train_poly, y_train)
      
      results[f"Poly_{degree}_X{i+1}"] = evaluate_model(model, X_train_poly, X_test_poly, y_train, y_test)