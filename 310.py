def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """

    if n == 1:
        return [0]

    dic = [set() for _ in range(n)]

    for x,y in edges:
        dic[x].add(y)
        dic[y].add(x)

    leaves = [i for i in range(n) if len(dic[i]) == 1]

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for i in leaves:
            node = dic[i].pop()
            dic[node].remove(i)
            if len(dic[node]) == 1:
                new_leaves.append(node)

        leaves = new_leaves

    return leaves

findMinHeightTrees(6, [[0,3],[1,3],[2,3],[4,3],[5,4]])
