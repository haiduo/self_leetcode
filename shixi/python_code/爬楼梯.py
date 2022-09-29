#1,2,3,4,5....

#迭代方法
def fib_i(N):
    a = 1
    b = 2
    if N < 3:
        return N
    for _ in range(2,N):
       a, b = b, a + b 
    return b

#递归方法
def fib_r(N):
    if N < 3:
        return N
    return fib_r(N-1) + fib_r(N-2)


if __name__ == '__main__':
    N = input("输入所查看的位置：")
    print(fib_i(int(N)))
    print(fib_r(int(N)))