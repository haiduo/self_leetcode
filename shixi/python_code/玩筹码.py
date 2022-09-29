def minCostToMoveChips(position):
    #偶数变偶数，奇数变奇数，没有代价
    #偶数变奇数，奇数变偶数，代价为1
    #所以，统计奇数和偶数的数量，取奇数和偶数数量较小的那个数量便是所求的代价
    oddCnt=0
    evenCnt=0
    for i in range(len(position)):
        if(position[i]%2!=0):
            oddCnt += 1
        else :
            evenCnt += 1
    return min(oddCnt,evenCnt)

if __name__ == '__main__':
    position = [1,2,3]
    print(minCostToMoveChips(position))
