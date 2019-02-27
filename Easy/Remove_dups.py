def removeDuplicates(nums):
    if nums==[]:
        return []
    temp=nums[0]
    #for i in range(len(nums)):
    #del nums[5:]
    #print (nums)
    index=0
    for i in range(len(nums)):
        if temp==nums[i]:
            continue
        else:
            nums[index]=temp
            temp=nums[i]
            index=index+1
    nums[index]=temp
    index=index+1
    del nums[index:]
    return nums

nums=[1,1,2,2,2,3,4,5,5,6,7]
print (removeDuplicates(nums))
