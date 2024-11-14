import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)  # Для воспроизводимости
n_samples = 100
X = np.random.normal(0, 1, n_samples).reshape(-1, 1)  # Генерация x из нормального распределения
y = 2 * X.squeeze() + 1 + np.random.normal(0, 1, n_samples)  # Генерация y как линейной функции от x с шумом

# трэйн, сплит что то там. В конце сказала валидация


# Разделение не тестовую 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание и обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)
print(model)


'''
   надо учить fit и predict
'''

#предсказание значений по тестовой выборке
y_pred = model.predict(X_test)

print(y_pred)
print(f"Коэффициенты модели: {model.coef_}")
print(f"Свободный член (intercept): {model.intercept_}")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# логистическая регрессия - это не регрессия, а классификация
# машина опорных векторов - randomForest
# svm, knn - самые простые алгоритмы
# knn - это про ближайших соседей 