def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    dic = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]

    for x,y in prerequisites:
        dic[x].append(y)

    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True

        visit[i] = -1
        for node in dic[i]:
            if not dfs(node):
                return False
        visit[i] = 1
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True

print(canFinish(2,[[1,0],[0,1]]))
