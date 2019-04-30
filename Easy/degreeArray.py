def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myDict={}
    for ind in range(len(nums)):
        i=nums[ind]
        if i in myDict.keys():
            myDict[i][0]=myDict[i][0]+1
            myDict[i][2]=ind
        else:
            myDict[i]=[1,ind,ind]
    
    myDict2={}
    for i in myDict.keys():
        if myDict[i][0] in myDict2.keys():
            myDict2[myDict[i][0]].append(i)
        else:
            myDict2[myDict[i][0]]=[i]
    
    
    solInd=max(myDict2.keys())
    
    #print solInd
    
    #print myDict2[solInd]
    
    myAns=50001
    
    for i in myDict2[solInd]:

        a=myDict[i][1]
        b=myDict[i][2]
        #print a,b
        
        if (b-a+1)<myAns:
            myAns=b-a+1
    
    return myAns
            
nums=[1,2,2,3,1]
print findShortestSubArray(nums)

nums=[1,2,2,3,1,4,2]
print findShortestSubArray(nums)