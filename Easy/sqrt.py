class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        res=2
        prev=1
        while(1):
            #print res,prev
            temp=res*res
            if temp<x:
                prev=res
                res=temp
                continue
            if temp==x:
                return res
            if temp>x:
                if res-prev==1:
                    return prev
                res=int((prev+res)/2)
                continue
                
        