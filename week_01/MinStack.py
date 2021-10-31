

from queue import Queue


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.list= []

    def push(self, x: int) -> None:
        self.list.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))

    def pop(self) -> None:
        self.list.pop()
        self.min.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()