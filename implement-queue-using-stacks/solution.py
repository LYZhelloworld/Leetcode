class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        # Stack 1 for pushing, Stack 2 for poping


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.__move()
        result = self.peek()
        del self.s2[-1]
        return result

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.__move()
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) + len(self.s2) == 0

    def __move(self):
        if len(self.s2) == 0:
            for i in range(len(self.s1)):
                self.s2.append(self.s1[-1])
                del self.s1[-1]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
