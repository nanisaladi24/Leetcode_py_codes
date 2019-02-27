def soln(strs):
    myLen = min([len(i) for i in strs])
    i=0
    soln=""
    if strs==[]:
        return ""
    while i < myLen:
        if len(set([k[i] for k in strs]))==1:
            soln=soln+strs[0][i]
            i=i+1
        else:
            break
    return soln

strs=["flower","flow","flight"]
print (soln(strs))