class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curr_min = self.getMin()
        if curr_min == None or x < curr_min:
            curr_min = x
        self.stack.append((x, curr_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack) - 1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1][1]

obj = MinStack()
obj.push(3)
obj.pop()
obj.push(2)
obj.push(-1)
obj.push(-2)
obj.push(3)
print(obj.getMin())
