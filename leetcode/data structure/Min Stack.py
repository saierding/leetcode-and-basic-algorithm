# 155. Min Stack


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_val = float("inf")

    def push(self, x: int):
        if x <= self.min_val:
            self.data.append(self.min_val)
            self.min_val = x

        self.data.append(x)

    def pop(self):
        if self.data[-1] == self.min_val:
            self.data.pop()
            self.min_val = self.data[-1]
            self.data.pop()
        else:
            self.data.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.min_val
