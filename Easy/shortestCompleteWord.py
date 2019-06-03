def shortestCompletingWord(licensePlate, words):
    """
    :type licensePlate: str
    :type words: List[str]
    :rtype: str
    """
    
    lMap={}
    
    for i in licensePlate:
        if i.isalpha():
            k=i.lower()
            if k in lMap.keys():
                lMap[k]=lMap[k]+1
            else:
                lMap[k]=1
    
    #print lMap
    
    # print set(lMap.keys())
    
    lSet=set(lMap.keys())
    
    myWrd=""
    myLen=16
    
    for w in words:
        
        tempSet=set(w)
        
        if lSet != tempSet.intersection(lSet):
            continue
            
        
        tempMap={}
        ct=0
        for i in w:
            ct=ct+1
            if i.isalpha():
                k=i.lower()
                if k in tempMap.keys():
                    tempMap[k]=tempMap[k]+1
                else:
                    tempMap[k]=1
        
        if myLen>ct:
            tempF=0
            for i in lMap.keys():
                #print lMap[i]
                #print tempMap[i]
                if lMap[i]<=tempMap[i]:
                    continue
                else:
                    tempF=1
                    break

            if tempF==0:
                myLen=ct
                myWrd=w
    
    return myWrd



licencePlate="Ah71752"
words=["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"]

print shortestCompletingWord(licencePlate,words)