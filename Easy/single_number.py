def singleNum(nums):
    myNum=0
    for i in nums:
        myNum=myNum^i
    return myNum

nums=[2,2,1]
print (singleNum(nums))