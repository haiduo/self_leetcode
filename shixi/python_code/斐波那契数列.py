#0,1,1,2,3,5....
import functools
import time

#迭代方法
def fib_i(N):
    a = 0
    b = 1
    if N in (0,1):
        return N
    for _ in range(1,N):
       a, b = b, a + b 
    return b

#递归方法
def fib_r(N):
    if N in (0,1):
        return N
    return fib_r(N-1) + fib_r(N-2)

#该函数是一个装饰器，为函数提供缓存功能。在下次以相同参数调用时直接返回上一次的结果.
@functools.lru_cache(maxsize=300) 
def fib_r_cache(N):
    if N in (0,1):
        return N
    return fib_r_cache(N-1) + fib_r_cache(N-2)


if __name__ == '__main__':
    # N = input("输入所查看的位置：")
    # print(fib_i(int(N)))
    # print(fib_r(int(N)))
    N = 34
    print(fib_i(int(N)))
    stime = time.time()
    print(fib_r(int(N)))
    print("total time is %.3fs" % (time.time() - stime))
    stime = time.time()
    print(fib_r_cache(int(N)))
    print("total time is %.3fs" % (time.time() - stime))