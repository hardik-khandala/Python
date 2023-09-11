def add_matrices(matrix1, matrix2):
  rows = len(matrix1)
  cols = len(matrix1[0])
  result = [[0 for i in range(cols)] for j in range(rows)]
  for i in range(rows):
    for j in range(cols):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

print(add_matrices(matrix1,matrix2))
