class MyCircularDeque:
    '''
    循环数组中任何时刻一定至少有一个位置不存放有效元素。
    判别队列为空的条件是：front == rear;；
    判别队列为满的条件是：(rear + 1) % capacity == front;。
    '''
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0] * self.capacity
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        #指针前移的时候，为了循环到数组的末尾，需要先加上数组的长度，然后再对数组长度取模。
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.rear] = value
        #指针后移的时候，下标 + 1+1，要取模；
        self.rear = (self.rear + 1) % self.capacity
        return True
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear
    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.rear + 1) % self.capacity == self.front

if __name__ == "__main__":
    obj = MyCircularDeque(3)
    print(obj.insertFront(1))
    print(obj.insertLast(2))
    print(obj.deleteFront())
    print(obj.deleteLast())
    print(obj.getFront())
    print(obj.getRear())
    print(obj.isEmpty())
    print(obj.isFull())