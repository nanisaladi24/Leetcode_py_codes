def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    #if no dups - return false
    # if dup found and index diff greater - update index
    # if dup found and index diff less - return true
    # else - return false
    
    myDict=set(nums)
    if len(myDict)==len(nums):
        return False
    
    myDict={}
    
    for i in range(len(nums)):
        if nums[i] in myDict.keys():
            if (i-myDict[nums[i]])>k:
                myDict[nums[i]]=i
                
            else:
                return True
        
        else:
            myDict[nums[i]]=i
    
    return False


nums=[1,2,3,4,1,4,2]
k=2
print containsNearbyDuplicate(nums,k)

nums=[1,2,3,1,2,4,2]
k=1
print containsNearbyDuplicate(nums,k)