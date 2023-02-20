'''
5.Tensorflow (створити набір даних (розмір за власним рішенням),
 провести CRUD операції над даними, reshape, інтеграцію np.array, pd.DataFrame)
'''
import tensorflow as tf
import pandas as pd

if __name__ == '__main__':
    data_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    tf_data = tf.constant(data_list)
    print(tf_data)

    # Отримання значень з Tensorflow об'єкту по індексу
    print('Отримання значень з Tensorflow об єкту по індексу\n', tf_data[0])

    # Заміна значення за індексом
    tf_data = tf.tensor_scatter_nd_update(tf_data, [[0]], [100])
    print('Заміна значення за індексом\n',tf_data)

    # Додавання значення в кінець об'єкту
    tf_data = tf.concat([tf_data, [60]], axis=0)
    print('Додавання значення в кінець об єкту\n', tf_data)

    # # Видалення значення за індексом(незрозуміла помилка)
    # tf_data = tf.tensor_scatter_nd_update(tf_data, [[0]], [ ])
    # print('Видалення значення за індексом\n', tf_data)

    # Видалення значення за індексом 0
    tf_data = tf.slice(tf_data, [1], [9])
    print('Видалення значення за індексом 0\n', tf_data)

    # Видалення значення за індексом 3
    slice1 = tf.slice(tf_data, [0], [2])
    # print(slice1)
    slice2 = tf.slice(tf_data, [3], [6])
    # print(slice2)
    tf_data = tf.concat([slice1, slice2], 0)
    print('Видалення значення за індексом 3\n', tf_data)

    # Перетворимо Tensorflow об'єкт у масив NumPy
    np_data = tf_data.numpy()
    print('Перетворимо Tensorflow обєкт у масив NumPy\n', np_data)

    # Pandas DataFrame з нашими даними
    df = pd.DataFrame(np_data, columns=['elements'])
    print('Pandas DataFrame з нашими даними\n', df)

    # Gроведемо операцію зміни форми (reshape) Tensorflow об'єкту
    tf_data_reshape = tf.reshape(tf_data, [2, 4])
    print('Gроведемо операцію зміни форми (reshape) Tensorflow об єкту\n', tf_data_reshape)

