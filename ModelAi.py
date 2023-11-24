import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

# Загрузим датасет рукописных цифр
digits = load_digits()

# Разделим данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Создадим модель многослойного персептрона (MLP)
model = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4, solver='sgd', random_state=42, learning_rate_init=0.1)

# Обучим модель
model.fit(X_train, y_train)

# Предскажем значения для тестовой выборки
y_pred = model.predict(X_test)

# Оценим точность модели
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f'Точность модели: {accuracy}')

# Визуализация изображений, предсказанных значений и фактических значений
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(8, 8), cmap='gray')
    ax.set_title(f'Факт: {y_test[i]}\nПредсказано: {y_pred[i]}')
    ax.axis('off')

plt.show()