import numpy as np

mat = 2 * np.eye(3)

inv = np.linalg.inv(mat)
solved = np.linalg.solve(mat, [1, 1, 1])
#solve(a, b) returns a matrix x such that ax = b

norm = np.linalg.norm(mat)
norm = np.linalg.norm(mat, np.inf) #infinity norm. Can use any number here

x = np.power(mat, 3) #raise matrix to the same power
x = np.power(mat, [[1, 2, 3],[1, 2, 4], [1, 2, 3]]) #raise matrix to a matrix of powers

x = mat @ mat #matrix multiplication
x = mat * mat #matrix hadamard product
x = mat - mat
x = mat + mat
x = 3 * mat

x = np.diag(mat)

