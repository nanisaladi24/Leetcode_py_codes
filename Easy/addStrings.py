def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num1=num1[-1::-1]
    num2=num2[-1::-1]
    # print num1
    # print num2
    car=0
    if len(num1)<len(num2):
        temp=num1
        num1=num2
        num2=temp
    sol=""
    k=len(num2)
    k=k-1
    #print k
    for i in range(len(num1)):
        a=0
        p=int(num1[i])
        if i>k:
            q=0
        else:
            q=int(num2[i])
        # print "pq"
        # print p
        # print q
        a=car+p+q
        # print a
        if a>9:
            car=1
            a=a-10
        else:
            car=0
        sol=str(a)+sol
        # print sol
    
    if car==1:
        sol="1"+sol
    # print sol
    
    return sol


p="108"
q="95"
print addStrings(p,q)
                