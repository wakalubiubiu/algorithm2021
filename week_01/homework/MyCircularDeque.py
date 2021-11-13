class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.list = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.list) == self.k:
            return False
        else:
            self.list.insert(0, value)
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.list) == self.k:
            return False
        else:
            self.list.append(value)
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.list) == 0:
            return False
        else:
            self.list.pop(0)
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.list) == 0:
            return False
        else:
            self.list.pop(len(self.list)-1)
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.list:
            return -1
        return self.list[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.list:
            return -1
        return self.list[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.list

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.list) == self.k