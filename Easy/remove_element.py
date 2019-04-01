def removeElement(nums, val):
    #currIdx=0
    prevIdx=0
    for i in range(len(nums)):
        if nums[i]==val:
            continue
            #currIdx=currIdx+1
        else:
            #nums[prevIdx]=nums[currIdx]
            nums[prevIdx]=nums[i]
            prevIdx=prevIdx+1
            #currIdx=currIdx+1
    return prevIdx

nums = [3,2,2,3]
print(nums[0:removeElement(nums,3)])
nums = [0,1,2,2,3,0,4,2]
print(nums[0:removeElement(nums,2)])