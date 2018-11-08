import math

def reverse(x):
    i=str(x)
    print i
    x=""
    if i[0]=='-':
        x=x+i[0]+i[len(i):0:-1]
    else:
        x=x+i[len(i):0:-1]+i[0]
    print x
    m=int(x)
    
    if m<(-math.pow(2,31))<=m<=(math.pow(2,31)-1):
        return m
    return 0 

print reverse(-120)