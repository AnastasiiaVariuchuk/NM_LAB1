'''
1.NumPy (створити набір даних (розмір за власним рішенням), провести CRUD операції над даними
 (скаляр, вектор, матриця)). Використати arange, random.
'''

import numpy as np

if __name__ == '__main__':
    # CREATE
    arr = np.array([[22, 10, 2002], [15, 9, 2003], [31, 8, 2003], [24, 10, 2001]])
    zeros_arr = np.zeros((3, 3))
    ones_arr = np.ones((3, 3))
    random_arr = np.random.randint(0, 10, (3, 3))
    arange_arr = np.arange(1, 12, 2).reshape((3, 2))
    print("CREATE\narr\n", arr, "\nzeros_arr\n", zeros_arr, "\nones_arr\n", ones_arr, "\nrandom_arr\n", random_arr,
          "\narange_arr\n", arange_arr)

    # READ
    elem = arr[1, 2]
    row = arr[1, :]
    col = arr[:, 2]
    matrix = np.asarray([row, row])
    print("READ\nelem\n", elem, "\nrow\n", row, "\ncol\n", col, "\nmatrix\n", matrix)

    # UPDATE
    arr[1, 2] = 1998
    print("UPDATE 1\n", arr)
    arr[2, :] = [28, 3, 1992]
    print("UPDATE 2\n", arr)
    arr[:, 1] = [11, 11, 11, 11]
    print("UPDATE 3\n", arr)

    # DELETE
    arr = np.delete(arr, 1, axis=0)
    print("DELETE 1\n", arr)
    arr = np.delete(arr, np.s_[::2], axis=1)
    print("DELETE 2\n", arr)
    arr = np.delete(arr, 0)
    print("DELETE 3\n", arr)
