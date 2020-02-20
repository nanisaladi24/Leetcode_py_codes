def openLock(deadends, target):
    """
    :type deadends: List[str]
    :type target: str
    :rtype: int
    """
    visited = set()
    
    deadends = set(deadends)
    
    if "0000" in deadends:
        return -1
    
    visited.add("0000")
    
    myQueue = []
    
    myQueue.append(["0000",0])
    
    while (myQueue!=[]):
        myStr = myQueue[0]
        myQueue=myQueue[1:]
        
        ct = myStr[1]
        
        if myStr[0] == target:
            return ct
        
        for i in range(4):
            myStr2 = list(myStr[0])
            
            #Sub -1
            if myStr2[i]=="0":
                myStr2[i]="9"
            else:
                myStr2[i] = str(int(myStr2[i])-1)
            
            myStr2 = "".join(myStr2)
            
            if (myStr2 in deadends) or (myStr2 in visited):
                pass
            else:
                visited.add(myStr2)
                myQueue.append([myStr2,ct+1])
            
            #print "2: "+myStr2
            
            myStr3 = list(myStr[0])
            
            #Add +1
            if myStr3[i]=="9":
                myStr3[i]="0"
            else:
                myStr3[i] = str(int(myStr3[i])+1)
            
            myStr3 = "".join(myStr3)
            
            if (myStr3 in deadends) or (myStr3 in visited):
                pass
            else:
                visited.add(myStr3)
                myQueue.append([myStr3,ct+1])
            
            #print "3: "+myStr3
        
        #print " ------ "
        
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

print (openLock(deadends,target))