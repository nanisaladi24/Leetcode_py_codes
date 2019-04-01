def majorEle(nums):
    if len(nums)==1:
        return nums[0]
    nums.sort()
    ct=1
    #print (nums)
    prev=nums[0]
    tot=int(len(nums)/2)+1
    for i in range(1,len(nums)):
        if prev==nums[i]:
            ct=ct+1
            if ct==tot:
                return prev
        else:
            prev=nums[i]
            ct=1


nums=[3,2,3]
print(majorEle(nums))