import heapq
from typing import List
import random

'''快速选择排序思想'''
def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[low]                                        # 选取最左边为pivot，初始化一个待比较数据
    left, right = low, high     # 双指针
    while left < right:
        while left<right and arr[right] >= pivot:          # 从后往前查找，直到找到一个比pivot更小的数
            right -= 1
        arr[left] = arr[right]                             # 将更小的数放入左边
        while left<right and arr[left] <= pivot:           # 从前往后找，直到找到一个比pivot更大的数
            left += 1
        arr[right] = arr[left]                             # 将更大的数放入右边    
    arr[left] = pivot           # 待比较数据放入最终位置 
    return left                 # 返回待比较数据最终位置

def randomPartition(arr: List[int], low: int, high: int) -> int:
    pivot_idx = random.randint(low, high)                   # 随机选择pivot
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]     # 将pivot的值与最左边值交换
    return partition(arr, low, high)                        # 调用partition函数

#topk切分
def topKSplit(arr: List[int], low: int, high: int, k: int) -> int:
    # mid = partition(arr, low, high)                   # 以mid为分割点【非随机选择pivot】
    mid = randomPartition(arr, low, high)               # 以mid为分割点【随机选择pivot】
    if mid == k-1:                                      # 第k小元素的下标为k-1
        return arr[mid]                                 #【找到即返回】
    elif mid < k-1:
        return topKSplit(arr, mid+1, high, k)           # 递归对mid右侧元素进行排序
    else:
        return topKSplit(arr, low, mid-1, k)            # 递归对mid左侧元素进行排序

#获取第k大元素
def findKthLargest(nums: List[int], k: int) -> int:
    n = len(nums)
    return topKSplit(nums, 0, n-1, n-k+1)        # 第k大元素即为第n-k+1小元素

#获得前k小的数
def topk_smalls(nums, k):
    topKSplit(nums, k, 0, len(nums)-1)
    return nums[:k]

#获得第k小的数
def topk_small(nums, k):
    topKSplit(nums, k, 0, len(nums)-1)
    return nums[k] 

#获得前k大的数 
def topk_larges(nums, k):
    #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
    topKSplit(nums, len(nums)-k, 0, len(nums)-1) # 把k换成len(nums)-k
    return nums[len(nums)-k:] 

#快速排序
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)

#只排序前k个小的数
#获得前k小的数O(n)，进行快排O(klogk)
def topk_sort_left(nums, k):
    topKSplit(nums, k, 0, len(nums)-1) 
    topk = nums[:k]
    quicksort(topk, 0, len(topk)-1)
    return topk+nums[k:] #只排序前k个数字

#只排序后k个大的数
#获得前n-k小的数O(n)，进行快排O(klogk)
def topk_sort_right(nums, k):
    topKSplit(nums, len(nums)-k, 0, len(nums)-1) 
    topk = nums[len(nums)-k:]
    quicksort(topk, 0, len(topk)-1)
    return nums[:len(nums)-k]+topk #只排序后k个数字


'''堆排序思想——大顶堆方法--静态数组'''
def findKthLargest_h_b( nums: List[int], k: int) -> int:
    def maxHeapify(arr, i, end):     # 大顶堆
        j = 2*i + 1                 # j为i的左子节点【建堆时下标0表示堆顶】
        while j <= end:             # 自上而下进行调整
            if j+1 <= end and arr[j+1] > arr[j]:    # i的左右子节点分别为j和j+1
                j += 1                              # 取两者之间的较大者
            if arr[i] < arr[j]:             # 若i指示的元素小于其子节点中的较大者
                arr[i], arr[j] = arr[j], arr[i]     # 交换i和j的元素，并继续往下判断
                i = j                       # 往下走：i调整为其子节点j
                j = 2*i + 1                 # j调整为i的左子节点
            else:                           # 否则，结束调整
                break
    n = len(nums)
    # 建堆【大顶堆】
    for i in range(n//2-1, -1, -1):         # 从第一个非叶子节点n//2-1开始依次往上进行建堆的调整
        maxHeapify(nums, i, n-1)

    # 排序：依次将堆顶元素（当前最大值）放置到尾部，并调整堆
    # k-1次重建堆（堆顶元素），或 k次交换到尾部（倒数第k个元素）
    for j in range(n-1, n-k-1, -1):
        nums[0], nums[j] = nums[j], nums[0]     # 堆顶元素（当前最大值）放置到尾部j
        maxHeapify(nums, 0, j-1)                 # j-1变成尾部，并从堆顶0开始调整堆
    
    return nums[-k]

#上面的等价方法
#堆的调用：https://blog.csdn.net/chandelierds/article/details/91357784
def findKthLargest_h_b_1(nums: List[int], k: int) -> int:
    if not nums:
        return []
    n =len(nums)
    h = []  #建立空堆
    for i in nums:
        heapq.heappush(h, i) #heappush自动建立小根堆
    sort_heap = [heapq.heappop(h) for _ in range(len(h))]  #heappop每次删除并返回列表中最小的值
    # print(sort_heap) #打印排序好的
    return sort_heap[n-k]

'''堆排序思想——小顶堆方法--动态数组'''
def findKthLargest_h_b_2(nums: List[int], k: int) -> int:
    if not nums:
        return []
    h = []  #建立空堆
    for i in nums:
        heapq.heappush(h, i) #heappush自动建立小根堆
        # print('ppo_b:',h)
        if len(h) > k:
            # print('ppo:',heapq.heappop(h))
            heapq.heappop(h) #保证每次的堆的大小都为k，则每轮的0位置的值都为所有的添进的第k大
            # print('ppo_h:',h)
    return h[0]

if __name__ == '__main__':
    list1 = [3,2,1,5,6,4]
    k1 = 2
    list2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4 
    print(findKthLargest(list1,k1))
    print(findKthLargest(list2,k2))
    print(findKthLargest_h_b(list1,k1))
    print(findKthLargest_h_b(list2,k2))
    print(findKthLargest_h_b_1(list1,k1))
    print(findKthLargest_h_b_1(list2,k2))
    print(findKthLargest_h_b_2(list1,k1))
    print(findKthLargest_h_b_2(list2,k2))