import collections

#两个队列
class MyStack1:
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
    #其中queue1用于存储栈内的元素,queue2作为入栈操作的辅助队列
    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self) -> int:
        return self.queue1.popleft()
    def top(self) -> int:
        return self.queue1[0]
    def empty(self) -> bool:
        return not self.queue1 #判断栈是否为空时，只需要判断queue 1是否为空即可。

class MyStack2:
    def __init__(self):
        self.queue = collections.deque()
    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n): #除了新入栈的元素之外的全部元素,依次出队并入队到队列
            self.queue.append(self.queue.popleft())
    def pop(self) -> int:
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        return not self.queue


if __name__ == "__main__":
    obj = MyStack1()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.top())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.empty())
    obj = MyStack2()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.top())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.empty())
