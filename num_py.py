import numpy as np

print("Matrix operations using NumPy")
mat_A = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat_B = np.array([[10,11,12],[13,14,15],[16,17,18]])

print("Matrix A : ")
print(mat_A)
print("\nMatrix B : ")
print(mat_B)

print("\nAddition :")
print(mat_A + mat_B)

print("\nMultiplication :")
print(mat_A.dot(mat_B))

print("\nTranspose :")
print(mat_A.transpose())
print(mat_B.transpose())
