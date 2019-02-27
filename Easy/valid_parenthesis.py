def soln(myStr):
    lookup1="[{("
    lookup2="]})"
    if myStr=="":
        return True
    myStack=list()
    # myStack.append(1)
    # myStack.pop()
    #print (myStack)
    if myStr[0] in lookup2:
        return False
    temp=""
    for i in myStr:
        if i in lookup1:
            myStack.append(i)
            temp=i
        if i in lookup2:
            if i==lookup2[lookup1.index(temp)]:
                myStack.pop()
                if len(myStack)>0:
                    temp=myStack[-1]
            else:
                return False
    if myStack==[]:
        return True
    else:
        return False

myStr="[]{}()"
print(soln(myStr))
myStr="[]{[]}]()"
print(soln(myStr))
myStr="[]{}([])"
print(soln(myStr))
myStr="[]{{{}}([])}"
print(soln(myStr))