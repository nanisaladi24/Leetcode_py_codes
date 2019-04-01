def reverseBits(n):
    # temp=0
    # ct=31
    # while n!=0:
    #     curr=n&1
    #     temp =temp|curr
    #     n=n>>1
    #     temp=temp<<1
    #     ct=ct-1
    # while ct!=0:
    #     temp=temp<<1
    #     ct=ct-1
    # #print (bin(temp))
    # return temp
    myStr=str(bin(n))
    myStr=myStr[2:]
    myStr=myStr[::-1]
    myStr='0b'+myStr+('0'*(32-len(myStr)))
    return int(myStr,2)


n=43261596
print(reverseBits(n))
n=4294967293
print(reverseBits(n))