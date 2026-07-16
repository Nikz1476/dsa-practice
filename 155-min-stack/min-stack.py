class MinStack(object):
    #O(1)
    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if self.minstack == []:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

