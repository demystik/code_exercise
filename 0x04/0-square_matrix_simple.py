def square_matrix_simple(matrix=[]):
    new_mat = matrix.copy()

    for i in range(len(new_mat)):
        new_mat[i] = list(map(lambda x : x ** 2, new_mat[i]))
    return new_mat
