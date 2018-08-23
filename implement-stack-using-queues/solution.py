class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = [] # Assume it is a queue. Only use append(), q[0], del q[0], and len(q)

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        size = len(self.q)
        self.q.append(x)
        for i in range(size):
            self.q.append(self.q[0])
            del self.q[0]

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        result = self.top()
        del self.q[0]
        return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
