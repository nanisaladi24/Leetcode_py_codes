def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    mySet=set(nums)
    
    if len(mySet)==len(nums):
        return False
    return True

nums=[1,2,3,4]
print containsDuplicate(nums)

nums=[1,2,3,4,1,4]
print containsDuplicate(nums)