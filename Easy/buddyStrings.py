def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if A==B=="":
        return False

    X=list(A)
    Y=list(B)
    
    m=set()

    if len(X)==len(Y):
        if A==B:
            for i in X:  
                if i in m:
                    return True
                else:
                    m.update(i)
            return False
        else:
            k=list()
            l=list()
            ct=2
            for i in range(len(X)):

                if X[i]==Y[i]:
                    continue
                elif ct!=0 and X[i]!=Y[i]:
                    k.append(X[i])
                    l.append(Y[i])
                    ct=ct-1
                else:
                    return False
            
            k.reverse()
            if l==k:
                return True
            else:
                return False
    
    else:

        return False

##Examples

A="aaaabc"
B="aaaacb"

print(buddyStrings(A,B))

A="aabaac"
B="aacaab"

print(buddyStrings(A,B))

A="avaabc"
B="axaacb"

print(buddyStrings(A,B))