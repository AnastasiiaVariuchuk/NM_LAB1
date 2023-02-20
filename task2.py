'''
2.Pandas (створити dataframe різними способами, провести маніпуляції з
даними (head, describe, iloc, loc ...))
'''
import pandas as pd

#Створення DataFrame зі списку
data1 = [['John', 25], ['Alice', 30], ['Bob', 35]]
df1 = pd.DataFrame(data1, columns=['Name', 'Age'])

#Створення DataFrame зі словника
data2 = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 35]}
df2 = pd.DataFrame(data2)

#Створення DataFrame з CSV-файлу
df3 = pd.read_csv(r'C:\Users\Admin\PycharmProjects\pythonProject3\task2.csv')

if __name__ == '__main__':
    #Виведення перших 5 рядків таблиці
    print('\nВиведення перших 5 рядків таблиці')
    print(df1.head())
    print(df2.head())
    print(df3.head())
    #Виведення описової статистики для числових колонок
    print('\nВиведення описової статистики для числових колонок')
    print(df1.describe())
    print(df2.describe())
    print(df3.describe())
    #Вибірка даних по номеру рядка та колонки
    print('\nВибірка даних по номеру рядка та колонки')
    print(df1.iloc[0, 1])  # виводить 25 (значення у першому рядку, другій колонці)
    print(df2.loc[1, 'Name'])  # виводить Alice (значення у 2 рядку, колонці з назвою 'Name')
    #Додавання нової колонки
    print('\nДодавання нової колонки')
    df1['Salary'] = [50000, 60000, 70000]
    print(df1.head())
    #Фільтрування даних за певними умовами
    print('\nФільтрування даних за певними умовами 1')
    print(df2[df2['Age'] > 30])  # вибірка даних для рядків, де вік більший за 30
    print('\nФільтрування даних за певними умовами 2')
    print(df1[df1['Salary'] < 65000])  # вибірка даних для рядків, де зарплата менша від 65000
    #Сортування даних по певній колонці
    print('\nСортування даних по певній колонці')
    print(df3.sort_values(by='Name'))  # сортування за ім`ям
