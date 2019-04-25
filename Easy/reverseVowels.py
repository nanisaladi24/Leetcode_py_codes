def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    if s=="" or len(s)==1:
        return s
    k=set(list("aeiouAEIOU"))
    
    s=list(s)
    
    i=0
    j=len(s)-1
        
    temp=""
    
    while(i<j):
        l=s[i]
        r=s[j]
        
        if (l in k) and (r in k):
            s[i]=r
            s[j]=l
            i=i+1
            j=j-1
            continue
        
        else:
            if (l not in k) and (r in k):
                i=i+1
                continue
            elif (l in k) and (r not in k):
                j=j-1
                continue
            else:
                i=i+1
                j=j-1
    
    return "".join(s)

s= "hello"
print (reverseVowels(s))

s= "LeetCOdE"
print (reverseVowels(s))