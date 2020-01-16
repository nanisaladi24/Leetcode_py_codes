#Divide Array in Sets of K Consecutive Numbers

from collections import defaultdict 

def printDict(myDict):
    for i in myDict.keys():
        print str(i)+" : "+str(myDict[i])
    
def isPossibleDivide(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    myDict = defaultdict() 
    myArr=[]
    for i in nums:
        try:
            myDict[i]=myDict[i]+1
        except:
            myDict[i]=1
            myArr.append(i)
    
    myArr.sort()
    #print myArr
    h=len(myArr)
    while myArr!=[]:
        #print myArr
        #printDict(myDict)
        myInd=0
        if k>h:
            return False
        m = myArr[0]
        ct = myDict[m]
        myDict[m]=0
        #print myDict[myArr[0]]
        for i in range(1,k):
            n=myArr[i]
            myDict[n] = myDict[n]-ct
            #print myDict[myArr[i]]
            if n-m!=1 or myDict[m]>myDict[n]:
                return False
            m=n
            if myDict[n]==0:
                myInd=i
        
        myArr = myArr[myInd+1:]
        h=h-myInd
        
    return True
        
arr = [1,2,3,3,4,4,5,6]
k = 4

print isPossibleDivide(arr,k)
        