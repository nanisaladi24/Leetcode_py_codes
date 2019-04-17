def helper(sol,curr,currInd,limit,param):
    n=param[0]
    withZero=param[1]
    myDict=param[2]
    if currInd==(limit-1):
        sol.append("".join(curr))
        #print sol
        return
    currInd=currInd+1
    # if currInd==2:
    #     print "yo"
    #     print curr[0]
    for i in withZero:
        curr[currInd]=i
        curr[n-currInd-1]=myDict[i]
        #print curr
        helper(sol,curr,currInd,limit,param)  
    
    return

    
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        myDict={}
        myDict['1']='1'
        myDict['6']='9'
        myDict['8']='8'
        myDict['9']='6'
        myDict['0']='0'
        
        nonZero=['1','6','8','9']
        withZero=['0','1','6','8','9']
        evenSet=["11","69","88","96"]
        oddSet=["0","1","8"]
        
        if n==0:
            return []
        if n==1:
            return oddSet
        if n==2:
            return evenSet
        if n==3:
            sol=[]
            temp="-"*3
            temp=list(temp)
            for i in evenSet:
                for k in oddSet:
                    temp[0]=i[0]
                    temp[2]=i[1]
                    temp[1]=k
                    sol.append("".join(temp))
            return sol
        
        sol=[]
        
        curr="-"*n
        curr=list(curr)
        
        currInd=0
        
        param = [n,withZero,myDict]
        
        #print param
        
        for i in nonZero:
            curr[currInd]=i
            curr[n-currInd-1]=myDict[i]
            #print curr
            if n%2==1:
                for k in oddSet:
                    curr[int(n/2)]=k
                    helper(sol,curr,currInd,int(n/2),param)
            else:
                #print "hello"
                helper(sol,curr,currInd,int(n/2),param)
        
        return sol
        
        
        