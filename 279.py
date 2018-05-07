def numSquares(n):
    """
    :type n: int
    :rtype: int
    """

    rooted = int(n**(0.5))
    curr = 0
    count = 0
    real_count = 0
    results = []

    def backtrack(curr, target, start, count, arr):
        if curr == target:
            arr.append(count)
            return

        for num in range(start, 0, -1):
            if num**2 + curr > target:
                continue
            else:
                curr += num**2
                count += 1
                backtrack(curr, target, num, count, arr)
                curr -= num**2
                count -= 1

    backtrack(curr, n, rooted, count, results)
    real_count = min(results)
    return real_count

print(numSquares(12))
