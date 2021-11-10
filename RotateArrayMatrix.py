def rotate(matrix, direction):
    mylist=[]
    new_mat = []
    if len(matrix) == 1 and  len(matrix[0]) == 1: return matrix
    if direction is 'clockwise':
        # print("direction is ", direction)

        if len(matrix) == len(matrix[0]):
            cl = len(matrix[0])
            rl = len(matrix)
        else:
            cl = len(matrix)
            rl = len(matrix[0])
        for i in range(rl):
            for j in range(cl-1, -1, -1):
                mylist.append(matrix[j][i])
            new_mat.append(mylist)
            mylist = []
        # print("clock ->", new_mat)
        return new_mat
        # return [[matrix[2][0], matrix[1][0], matrix[0][0]], [matrix[2][1], matrix[1][1], matrix[0][1]], [matrix[2][2], matrix[1][2], matrix[0][2]]]
    else:
        # print("direction is ", direction)
        for i in range(len(matrix[0])-1, -1, -1):
            for j in range(len(matrix)):
                mylist.append(matrix[j][i])
            new_mat.append(mylist)
            mylist = []
        # print("anti-clock ->", new_mat)
        return new_mat
        # return [[matrix[0][2], matrix[1][2], matrix[2][2]], [matrix[0][1], matrix[1][1], matrix[2][1]], [matrix[0][0], matrix[1][0], matrix[2][0]]]

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]
print(rotate(matrix, 'counter-clockwise'), [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]])
print(rotate(matrix, 'clockwise'), [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix, 'counter-clockwise'), [[3, 6, 9], [2, 5, 8], [1, 4, 7]])
print(rotate(matrix, 'clockwise'), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
print(rotate(rotate(matrix, 'counter-clockwise'), 'clockwise'), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(rotate(rotate(rotate(rotate(matrix, 'clockwise'), 'clockwise'), 'clockwise'), 'clockwise'), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])



matrix = [[1, 2, 3]]
print(rotate(matrix, 'counter-clockwise'), [[3], [2], [1]])
print(rotate(matrix, 'clockwise'), [[1], [2], [3]])
print(rotate(rotate(matrix, 'clockwise'), 'clockwise'), [[3, 2, 1]])

matrix = [[1]]
print(rotate(matrix, 'counter-clockwise'), [[1]])