def revFlip(s):
    #s.reverse()
    #print s
    t=len(s)
    for i in range(int(t/2)):
        
        j=t-1-i
        
        l=s[i]
        r=s[j]
        
        if l:
            l=0
        else:
            l=1
        
        if r:
            r=0
        else:
            r=1
            
        s[i]=r
        s[j]=l
    
    if t%2==1:
        j=int(t/2)
        if s[j]:
            s[j]=0
        else:
            s[j]=1         
    
    return s

def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    #print A
    for i in range(len(A)):
        #print A[i]
        A[i]=revFlip(A[i])
    
    return A

A=[[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(A))

A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(A))