import math

def myAtoi(str1):
    """
    :type str: str
    :rtype: int
    """
    a="0123456789"
    l="-+"

    x=""
    f1=0
    f2=0
    for i in str1:
        if (not(f1==1 or f2==1)) and i==' ':
            #print 'a'
            continue
        elif (f1==1 or f2==1) and i==' ':
            #print 'a'
            break
        elif i not in (l+a):
            #print 'b'
            break
        elif f1==0 and f2==0 and (i in l):
            #print 'c'
            x=x+i
            f2=1
        elif (f1==1 or f2==1) and (i in l):
            #print 'd'
            break
        elif f1==0 and i in a:
            #print 'e'
            x=x+i
            f1=1
        elif i in a:
            x=x+i

    print x

    if x=="" or x=="-" or x=="+":
        return 0
    if x[0]=="+":
        x=x[1:]
    m=int(x)
    if m<(-math.pow(2,31)):
        return int((-math.pow(2,31)))
    elif m>(math.pow(2,31)-1):
        return int((math.pow(2,31)-1))
    return m

str1="+1"

print myAtoi(str1)