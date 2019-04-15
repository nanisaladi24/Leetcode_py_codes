import math

def helper(sol,curr,currInd,limit,param):
    n=param[0]
    withZero=param[1]
    myDict=param[2]
    up=param[3]
    down=param[4]
    if currInd==(limit-1):
        if (down<=int("".join(curr))<=up):
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
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
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
        
        # low_digit=math.floor(math.log(low))
        # high_digit=math.floor(math.log(high))
        
        if low=="0":
            low_digit=1
            low_no=0
        else:
            low_digit=int(math.log(int(low),10))+1
            low_no=int(low)
        if high=="0":
            high_digit=1
            high_no=0
        else:
            high_digit=int(math.log(int(high),10))+1
            high_no=int(high)

        #print low_digit
        #print high_digit
        
        myRes=0
        
        for n in range(low_digit,high_digit+1):
            
            #print n
            
            if n==0:
                continue
            if n==1:                
                if n==low_digit:
                    for i in oddSet:
                        if high_no>=int(i)>=low_no:
                            myRes=myRes+1
                else:
                    myRes=myRes+len(oddSet)
                continue
                
            if n==2:
                if n==low_digit:
                    for i in evenSet:
                        if high_no>=int(i)>=low_no:
                            myRes=myRes+1
                else:
                    myRes=myRes+len(evenSet)
                continue
                
            if n==3:
                sol=[]
                temp="-"*3
                temp=list(temp)
                for i in evenSet:
                    for k in oddSet:
                        temp[0]=i[0]
                        temp[2]=i[1]
                        temp[1]=k
                        if high_no>=int("".join(temp))>=low_no:
                            sol.append("".join(temp))
                myRes=myRes+len(sol)
                continue

            sol=[]

            curr="-"*n
            curr=list(curr)

            currInd=0

            param = [n,withZero,myDict,high_no,low_no]

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

            myRes=myRes+len(sol)
            #print myRes
        
        return myRes
        
        
                