def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if s=="":
        return True
    
    k=""
    j=""
    m=len(s)
    for i in range(m):
        if s[i].isalnum():
            k=k+s[i].lower()
        if s[m-i-1].isalnum():
            j=j+s[m-i-1].lower()
    #print j
    #print k
    if j==k:
        return True
    
    return False

myStr = "race a car"
myStr1 = "lol"

print isPalindrome(myStr)
print isPalindrome(myStr1)