'''
3. Matplotlib (створити набір даних лінійної функції з урахуванням помилок вимірювань,
побудувати графік функції та згенерованих даних, обчислити похибку з використанням
метрик MAE, MSE). Записати отримані результати у csv файл (формат: X,Y, Y_hat, mAE, mSE)
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

if __name__ == '__main__':
    # Встановлюємо випадковий генератор NumPy для повторюваності результатів
    np.random.seed(0)
    # Генеруємо 50 рівномірно розподілених значень від 0 до 10 для X
    X = np.linspace(0, 10, 50)
    # Генеруємо випадкові значення помилок вимірювань
    errors = np.random.normal(0, 1, 50)
    # Визначаємо лінійну функцію Y = 2X + 1 з додаванням помилок вимірювань
    Y = 2 * X + 1
    Y_errors = 2 * X + 1 + errors

    # Побудова графіку даних Y з помилками вимірювань
    plt.plot(X, Y, color='blue', label='Функція Y')
    plt.scatter(X, Y_errors, color='red', label='Дані Y+errors')
    plt.legend()
    plt.show()

    # Обчислення похибки MAE
    mae = mean_absolute_error(Y_errors, Y)
    # Обчислення похибки MSE
    mse = mean_squared_error(Y_errors, Y)

    print('MAE:', mae)
    print('MSE:', mse)

    df = pd.DataFrame({'X': X,
                       'Y': Y,
                       'Y_errors': Y_errors,
                       'mAE': mae,
                       'mSE': mse})

    df.to_csv(r'C:\Users\Admin\PycharmProjects\pythonProject3\task3.csv', index=False)


