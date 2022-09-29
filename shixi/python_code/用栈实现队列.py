#方法一（使用两个栈 入队 -O(n)， 出队 - O(1)）
class MyQueue1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = [] #栈1
        self.s2 = [] #栈2
        self.front = None
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1: 
            self.front = x
        while(self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while(self.s2):
            self.s1.append(self.s2.pop())
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """ 
        if self.s1:
            temp = self.s1.pop()
            if self.s1:
                self.front = self.s1[-1]
        return temp
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.s1:
            return True
        return False


#方法二 摊还分析 摊还分析的核心在于，最坏情况下的操作一旦发生了一次，
#那么在未来很长一段时间都不会再次发生，这样就会均摊每次操作的代价。入队 -O(1)， 出队 - O(1)
class MyQueue2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1: 
            self.front = x
        self.s1.append(x)
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.front = None
        return self.s2.pop()
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2: 
            return self.s2[-1]
        return self.front
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.s1 and not self.s2:
            return True
        return False

if __name__ == "__main__":
    obj = MyQueue1()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.peek())
    print(obj.empty())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.empty())
    print("摊还复杂度：")
    obj = MyQueue2()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.peek())
    print(obj.empty())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.empty())