def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """

    if not people:
        return []

    dict = {}
    height = []
    arr = []

    for i in range(len(people)):
        person = people[i]
        if person[0] in dict:
            dict[person[0]].append((person[1], i))
        else:
            dict[person[0]] = [(person[1], i)]
            height.append(person[0])

    height.sort(reverse=True)
    for h in height:
        dict[h].sort()
        print(dict[h])
        for person in dict[h]:
            arr.insert(person[0], people[person[1]])

    return arr

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
