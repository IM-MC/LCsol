def findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    if not matrix or len(matrix[0]) == 0:
        return []

    row = 0
    col = 0
    arr = []
    m = len(matrix)
    n = len(matrix[0])
    times = m*n

    for i in range(times):
        arr.append(matrix[row][col])
        if (row+col)%2 == 0: #go up
            if col == n - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == m - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                col -= 1
                row += 1

    return arr
