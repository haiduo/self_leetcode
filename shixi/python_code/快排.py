# 指针left：从左到右找大于pivote 的值
# 指针right：从右到左找小于pivote 的值
def getPartitionIndex(arr, left, right):
    pivote = arr[left]
    while left < right:
        while arr[right]  >= pivote and right > left:
            right -= 1
        arr[left] = arr[right]
        while arr[left] <= pivote and right > left:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivote
    return left

def quickSort(arr, left=None, right=None):
    print(arr)
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right

    if left < right:
        partitionIndex = getPartitionIndex(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

if __name__ == '__main__':
    arr = [3,2,1,-5,0,4,9,8]
    print(quickSort(arr))