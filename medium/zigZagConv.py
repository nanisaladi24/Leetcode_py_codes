def zigZagConv(s,r):
    if r==1:
        return s
    x=""
    for row in range(r):
        l=0
        f=0
        i=0
        while l<len(s):
            if row==0 or row==(r-1):
                l=(r+r-2)*i + row
                if l<len(s):
                    x=x+s[l]
                else:
                    break
                i=i+1
            else:
                if f==0:
                    l=(r+r-2)*i + row 
                    if l<len(s):
                        x=x+s[l]
                    else:
                        break
                    f=1
                    i=i+1
                else:
                    l=(r+r-2)*i - row 
                    if l<len(s):
                        x=x+s[l]
                    else:
                        break
                    f=0
    
    return x

s="PAYPALISHIRING"

print zigZagConv(s, 3)                    