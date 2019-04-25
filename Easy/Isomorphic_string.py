def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    myDict={}
    
    for i in range(len(s)):
        if s[i] in myDict.keys():
            if myDict[s[i]]==t[i]:
                continue
            else:
                return False
        elif t[i] in myDict.values():
            return False
        else:
            myDict[s[i]]=t[i]
            
    return True

s="egg"
t="add"

print (isIsomorphic(s,t))

s="foo"
t="bar"

print (isIsomorphic(s,t))

s="paper"
t="title"

print (isIsomorphic(s,t))