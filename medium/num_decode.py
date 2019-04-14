def is_valid(prev,curr):
    if prev==1 and 0<=curr<10:
        return True
    if prev==2 and 0<=curr<7:
        return True
    return False

def num_decode(s):
    if s=="" or s[0]=="0":
        return 0
    if len(s)==1:
        return 1
    
    pl,l=1,1
    for i in range(1,len(s)):
        curr=int(s[i])
        prev=int(s[i-1])
        temp1=0
        temp2=0
        if curr!=0:
            temp1=l
        if is_valid(prev,curr):
            temp2=pl
        pl=l
        l=temp1+temp2
        if l==0:
            return 0
        
    return l
        



s="227"
print (num_decode(s))

s="110"
print (num_decode(s))

s="1212"
print (num_decode(s))

s="24726"
print (num_decode(s))