def climbStairs(n): #Fibonacci logic
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    v1=1
    v2=2
    for i in range(3,n+1):
        temp=v2
        v2=v1+temp
        v1=temp
    return v2

n=3
print (climbStairs(n))