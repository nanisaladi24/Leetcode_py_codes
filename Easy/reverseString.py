def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    size = len(s)
    temp1=""
    temp2=""
    temp=""
    for i in range(int(size/2)):
        temp1=s[i]
        temp2=s[size-1-i]
        s[i]=temp2
        s[size-1-i]=temp1
        #print s
    
    return s

myStr="hellofjgkddf"
myStr=list(myStr)
print (reverseString(myStr))