
#类似爬楼梯
def translateNum(num: int) -> int: #从左向右遍历
    s = str(num)
    a = b = 1
    for i in range(2, len(s) + 1):
        a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
    return a

def translateNum1(num: int) -> int: #从右向左 遍历
        s = str(num)
        a = b = 1
        for i in range(len(s) - 2, -1, -1):
            a, b = (a + b if "10" <= s[i:i + 2] <= "25" else a), a
        return a

#改进版本-数字求余 空间复杂度为1
def translateNum_c( num: int) -> int:
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a

if __name__ == '__main__':
    N = 12258
    print(translateNum(N))
    print(translateNum_c(N))


