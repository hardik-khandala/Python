def transpose_matrix(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  transposed_matrix = [[0 for i in range(rows)] for j in range(cols)]
  for i in range(rows):
    for j in range(cols):
      transposed_matrix[j][i] = matrix[i][j]
  return transposed_matrix


matrix = [[1, 2, 3], [4, 5, 6]]

transposed_matrix = transpose_matrix(matrix)

print(transposed_matrix)
