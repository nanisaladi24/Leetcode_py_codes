"""
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. Includes 1.
"""

def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num==0:
        return False
    
    while num!=1 and num!=2 and num!=3 and num!=5:
        #print num
        if num%2==0:
            num=num/2
            continue
        
        elif num%3==0:
            num=num/3
            continue
        
        elif num%5==0:
            num=num/5
            continue
        
        else:
            return False
    
    return True


num=6
print (isUgly(num))

num=8
print (isUgly(num))

num=14
print (isUgly(num))