def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    mySumMap={}
    
    curr=0
    
    tot=0
    
    for i in nums:
        
        curr=curr+i
        
        if curr==k:
            tot=tot+1
            #print "yo"
            try:
                tot=tot+mySumMap[0]
            except:
                #print "exc1"
                pass
        
        else:
            try:
                tot=tot+mySumMap[curr-k]
            except:
                #print "exc2"
                pass
                
        try:
            mySumMap[curr]=mySumMap[curr]+1
        except:
            mySumMap[curr]=1
            #print "exc3"
    
    return tot


nums = [1,1,1]
k = 2

print subarraySum(nums,k)