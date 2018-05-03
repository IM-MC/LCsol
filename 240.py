def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    col = len(matrix[0]) - 1
    row = 0

    while col >= 0 and row <= len(matrix) - 1:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1

    return False

print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,25],[18,21,23,26,30]], 20))
