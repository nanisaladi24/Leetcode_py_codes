import math

def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    
    if n==1 or n==0:
        return n
    
    k = int(math.sqrt(n))
    
    myArr = []
    
    h=0
    
    for i in range(k+1):
        myArr.append(i*i)
        h=h+1
    
    myQueue = list()
    
    myQueue.append([0,0])
    
    visited = set()
    
    visited.add(0)
        
    while (myQueue!=[]):
        curr = myQueue[0]
        myQueue = myQueue[1:]
        
        if curr[0] == n:
            return curr[1]
        
        for i in range(h):
            
            m = curr[0]+myArr[i]
            
            if m>n:
                continue
            
            if m in visited:
                pass
            else:
                visited.add(m)
                myQueue.append([m,curr[1]+1])
    
    return n

n= 5479

print (numSquares(n))