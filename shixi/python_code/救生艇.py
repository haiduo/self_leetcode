from typing import List

#快排双指针解法
def numRescueBoats1(people: List[int], limit: int) -> int: 
    if people is None or len(people) == 0:
        return 0
    people.sort()
    left, right = 0, len(people)-1  #分别指向最轻、最重的人的下标
    while (left <= right):
        if people[left]+people[right] <= limit: 
            left= left+ 1
        right=right-1 #right既是当前排最重的人走的下标，也是乘船的数量
    return len(people)-1-right

if __name__ == '__main__':
    people = [3,2,2,1]
    limit = 3
    print(numRescueBoats1(people, limit))
    people = [2,1]
    limit = 3
    print(numRescueBoats1(people, limit))

