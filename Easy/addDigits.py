def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    if num==0:
        return 0
    k=num%9
    if k==0:
        return 9
    else:
        return k

num=478596
print (addDigits(num))

num=0
print (addDigits(num))

num=999
print (addDigits(num))