def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    dic = [set() for _ in range(numCourses)]
    neigh = [set() for _ in range(numCourses)]

    for x,y in prerequisites:
        dic[x].add(y)
        neigh[y].add(x)

    stack = [i for i in range(numCourses) if not dic[i]]
    arr = []

    while stack:
        node = stack.pop()
        arr.append(node)
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                stack.append(i)

    for element in dic:
        if len(element) != 0:
            return []

    return arr
    

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
