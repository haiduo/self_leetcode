from collections import deque
class RecentCounter:
    def __init__(self):
        self.req = []  # 用于存放请求

    def ping(self, t: int) -> int:
        self.req.append(t)  # 先将请求添加的列表
        while t-self.req[0] > 3000:  # 循环判断是否有超出3000ms的请求
            del self.req[0]  # 删除超出的请求
        return len(self.req)  # 返回3000ms以内的请求

class RecentCounter1: #python自带的双端队列，但此题只需要单端队列
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while t-self.q[0] > 3000:
            self.q.popleft()
        return len(self.q)


if __name__ == "__main__":
    obj = RecentCounter()
    t = [1, 100, 3001, 3002] #["ping", "ping", "ping", "ping"]
    for i in t:
        print(obj.ping(i))
    print("=======")
    obj1 = RecentCounter1()
    for i in t:
        print(obj1.ping(i))

