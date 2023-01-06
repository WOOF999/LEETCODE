def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return start

li=[1,3,5,7]
target = 6
idx=searchInsert(li,target)
print(idx)
