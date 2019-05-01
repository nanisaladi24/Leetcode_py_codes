# Longest palindrome sub sequence

def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    n=len(s)
    myL=[[0]*n for i in range(n)]
    
    #print myL
    
    #diagonal are 0
    for i in range(n):
        myL[i][i]=1
    
    for j in range(1,n): #col
        for i in range(0,n-j):  #row
            start=i
            end=j+i
            
            if s[start]==s[end]:
                myL[start][end]=myL[start+1][end-1]+2
            
            else:
                myL[start][end]=max((myL[start+1][end]),(myL[start][end-1]))
    
    #print myL
    
    res=myL[0][n-1]
    if res==0:
        return 1
    return res

myStr="aaaba"
print longestPalindromeSubseq(myStr)

myStr="a"
print longestPalindromeSubseq(myStr)