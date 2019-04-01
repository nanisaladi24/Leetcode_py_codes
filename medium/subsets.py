def getIndx(num):
    myIdx=[]
    ct=0
    while num!=0:
        if num&1==1:
            myIdx.append(ct)
        ct=ct+1
        num=num>>1
    return myIdx

def subsets(nums):
    if len(nums)==0:
        return []
    else:
        myList=[]
        myNum=1
        while myNum<2**(len(nums)):
            myNum=myNum<<1
        # print (myNum)
        for i in range(1,myNum):
            print (i)
            idxSet=getIndx(i)
            tempSet=[]
            for k in idxSet:
                tempSet.append(nums[k])
            myList.append(tempSet)
        return myList
            



#print(getIndx(486934))

nums=[1,2,3]
print (subsets(nums))