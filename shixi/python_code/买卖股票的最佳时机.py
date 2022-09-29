from typing import List

#一次遍历:
def maxProfit(prices: List[int]) -> int:
    inf = int(1e9)
    minprice = inf #最低点买进的
    maxprofit = 0 #最大获利
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))