def nth_largest(nums,k):
    if len(nums)==1:
        return nums[0]
    curr=nums[0]
    arr1=list()
    arr2=list()
    for i in nums[1:]:
        if i<curr:
            arr1.append(i)
        else:
            arr2.append(i)
    myIndex=len(arr2)+1
    # print k
    # print arr1
    # print arr2
    # print myIndex
    if k<myIndex:
        return nth_largest(arr2,k)
    elif k>myIndex:
        return nth_largest(arr1,k-myIndex)
    else:
        return curr


nums = [10,5,2,6,15,11,3]    

print (nth_largest(nums,2))
print (nth_largest(nums,1))
print (nth_largest(nums,4))
print (nth_largest(nums,3))

nums = [-1,-1]    

print (nth_largest(nums,2))

nums = [3,2,3,1,2,4,5,5,6]

print (nth_largest(nums,4))