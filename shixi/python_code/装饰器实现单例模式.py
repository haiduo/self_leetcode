def singleton(cls):
    '''创建一个单例模式'''
    def single_wrapper(*args, **kwargs):
        if not single_wrapper.instance:
            single_wrapper.instance = cls(*args, **kwargs)
        return single_wrapper.instance
    single_wrapper.instance = None
    return single_wrapper

@singleton
class Counter():
    def __init__(self):
        self._count = 0

    def visit(self):
        self._count += 1
        print(f'visiting: {self._count}')

if __name__ == "__main__":
    c1 = Counter()
    c1.visit()
    c1.visit()

c2 = Counter()
c2.visit()
c2.visit()