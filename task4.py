'''
4.Sklearn (провести вирішення задачі регресії та класифікації)
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

if __name__ == '__main__':
    # Завантажуємо дані та розділяємо їх на тренувальну та тестову вибірки
    X, y = fetch_california_housing(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    # Створюємо модель та навчаємо її на тренувальних даних
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Перевіряємо якість моделі на тестових даних
    print("Score for fetch_california_housing:", model.score(X_test, y_test))

    # Завантажуємо дані та розділяємо їх на тренувальну та тестову вибірки
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Створюємо модель та навчаємо її на тренувальних даних
    model = SVC()
    model.fit(X_train, y_train)

    # Перевіряємо якість моделі на тестових даних
    print("Score fro load_iris:", model.score(X_test, y_test))
