__author__ = 'responsible'
class MinStack(object):
    #Beacuse be asked to retrieve the minimum element in constant time
    #the stack element is like [element, minValueInStack]
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
        if len(self.stack) == 0:
            self.stack.append([x, x])
        else:
            self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        """
        :rtype: nothing
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]