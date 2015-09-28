__author__ = 'responsible'
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.empty():
            self.stack.append(x)
        else:
            stack1 = self.stack[-1::-1]
            self.stack = []
            self.stack.append(x)
            self.stack.extend((stack1)[-1::-1])

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0