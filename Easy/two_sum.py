from _collections import defaultdict
def two_sum(nums,target):
    dic = defaultdict()
    for i in range(len(nums)):
        if target-nums[i] in dic.keys():
            return [dic[target-nums[i]],i]
        else:
            dic[nums[i]]=i
    return []
    

nums=[2,7,11,15]
target=9
a=two_sum(nums, target)
print "hello world"
print a