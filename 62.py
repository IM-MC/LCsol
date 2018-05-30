def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    memo = [ [0] * n for _ in xrange(m)]

    def findPath(memo, index1, index2):

        if memo[index1][index2] != 0:
            return memo[index1][index2]

        if index1 >= m-1:
            return 1
        if index2 >= n-1:
            return 1

        #go down
        memo[index1+1][index2] = findPath(memo, index1+1, index2)
        #go right
        memo[index1][index2+1] = findPath(memo, index1, index2+1)

        memo[index1][index2] = memo[index1+1][index2] + memo[index1][index2+1]

        return memo[index1][index2]

    memo[0][0] = findPath(memo, 0, 0)
    return memo[0][0]

print(uniquePaths(7,3))
