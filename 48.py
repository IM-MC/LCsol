def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    length = len(matrix) - 1

    for i in range(0, int(len(matrix) / 2)):
        temp = matrix[length - i]
        matrix[length - i] = matrix[i]
        matrix[i] = temp

    for i in range(len(matrix)):
        for j in range(0, i):
            if i != j:
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(arr)

for row in arr:
    print(row)
