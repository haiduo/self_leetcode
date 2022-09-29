import functools
from typing import List

#记忆化搜索-动态规划 （自顶而下）
def coinChange1(coins: List[int], amount: int) -> int:
    #该函数是一个装饰器，为函数提供缓存功能。在下次以相同参数调用时直接返回上一次的结果.
    @functools.lru_cache(amount)
    def dp(remain) -> int:
        if remain < 0: return -1
        if remain == 0: return 0
        mini_count = int(1e9)
        for coin in coins:
            res = dp(remain - coin)
            if res >= 0 and res < mini_count:
                mini_count = res + 1
        return mini_count if mini_count < int(1e9) else -1

    if amount < 1: return 0
    return dp(amount)

#动态规划 （自底而上）
def coinChange2(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1) #根据之前计算的面值结果来计算当前面值的最优选择
    return dp[amount] if dp[amount] != float('inf') else -1 


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange1(coins, amount))
    print(coinChange2(coins, amount))