def isMonotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    flag=0
    
    prev=A[0]
    for i in A:
        
        if prev==i:
            prev=i
            continue
        
        if prev<i:
            if flag==1:
                prev=i
                continue
            if flag==0:
                flag=1
                prev=i
                continue
            else:
                return False
        
        if prev>i:
            if flag==2:
                prev=i
                continue
            if flag==0:
                flag=2
                prev=i
                continue
            else:
                return False
    
    return True

A=[6,5,4,4]
print (isMonotonic(A))

A=[1,3,2]
print (isMonotonic(A))