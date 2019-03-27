def fact(n):
    if n==1 or n==0:
        return 1
    else:
        res=1
        for i in range(2,n+1):
            res=res*i
        return res
def combi(n,r):
    k = r if r>(n-r) else (n-r)
    temp=1
    for i in range (k+1,n+1):
        temp=temp*i
    temp2 = fact(n-k)
    return int(temp/temp2)

def uniquePath(m,n):
    p=m-1
    q=n-1
    tot = p+q
    return combi(tot,p)

m=3
n=2
print (uniquePath(m,n))
