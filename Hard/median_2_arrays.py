def median_sort_two(A,B):
    m,n=len(A),len(B)
    if m>n:
        A,B,m,n=B,A,n,m
    
    imin,imax,half_len=0,m,(m+n+1)/2
    while imin<=imax:
        i=(imin+imax)/2
        j=half_len-i
        if j>0 and i<m and B[j-1]>A[i]:
            imin=i+1
        elif i>0 and j<n and A[i-1]>B[j]:
            imax=i-1
        else:
            if i==0:
                num1=B[j-1]
            elif j==0:
                num1=A[i-1]
            else:
                num1=max(A[i-1],B[j-1])
            
            if (m+n)%2==1:
                return num1
            
            if i==m:
                num2=B[j]
            elif j==n:
                num2=A[i]
            else:
                num2=min(A[i], B[j])
            
            return (num1+num2)/2.0
        

A=[1,2]
B=[3]

print median_sort_two(A, B)
    