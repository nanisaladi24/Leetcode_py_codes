def maxSubArr(nums):
    if len(nums)==1:
        return nums[0]
    bestSumHere = nums[0]
    bestNetSum = nums[0]
    for i in nums[1:]:
        bestSumHere = max(bestSumHere+i,i)
        bestNetSum = max(bestSumHere,bestNetSum)
    return bestNetSum


A=[1,76,42,4,-6,34-23,5]
print (maxSubArr(A))