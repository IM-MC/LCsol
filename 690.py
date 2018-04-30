"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
def getImportance(employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """

    map = {empoloyee.id: empoloyee for employee in empoloyees}
    priority = 0
    stack = [map[id]]
    while stack:
        top = stack.pop()
        priority += top.importance
        for i in top.subordinates:
            stack.append(map[i])

    return priority
