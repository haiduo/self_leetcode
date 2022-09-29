#两次遍历
def moveZeroes1(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    # 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]	
    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j] = nums[i]
            j += 1
    # 非0元素统计完了，剩下的都是0了
    # 所以第二次遍历把末尾的元素都赋为0即可
    for i in range(j,len(nums)):
        nums[i] = 0
    return nums

#一次遍历,快速排序的思想
def moveZeroes2(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    # 两个指针i和j
    j = 0
    for i in range(len(nums)):
        # 当前元素!=0，就把其交换到左边，等于0的交换到右边
        if nums[i]:
            if (i > j): #改进，减少交换次数
                nums[j],nums[i] = nums[i],nums[j]
            j += 1

    return nums

if __name__ == '__main__':
    list1 = [0,1,0,3,12]
    print(moveZeroes1(list1))
    print(moveZeroes2(list1))