import heapq
#首先是一个完全二叉树，其次满足每一个节点大于（大顶堆）或小于（小顶堆）所有孩子节点
def test():
    # Create minheap 最小堆（最大堆只需将列表数值取反，取出时再求反）
    minheap = []
    heapq.heapify(minheap)
    
    # Add element
    heapq.heappush(minheap, 10)
    heapq.heappush(minheap, 8) 
    heapq.heappush(minheap, 9)
    heapq.heappush(minheap, 2)
    heapq.heappush(minheap, 1)
    heapq.heappush(minheap, 11)
    
    #[1,2,9,10,8,11]
    print(minheap)
    
    # peek 取堆顶 1
    print(minheap[0])
    
    # Delete 删除堆顶，构建新的堆
    heapq.heappop(minheap)
    print('删除后：',minheap)
    
    # Size 
    len(minheap)

    # Iteration 遍历
    print('Iteration:')
    while len(minheap) != 0:
        print(heapq.heappop(minheap))

if __name__ == '__main__':
    test()