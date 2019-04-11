class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

def printList(k):
    mystr=""
    while k!=None:
        mystr=mystr+str(k.val)+"-"
        k=k.next
    print (mystr)
    return

def merge2Lists(i,j):
    if i==j==None:
        return None
    res=ListNode(0)
    prev=None
    myres=res
    while i!=None or j!=None:
        if i!=None and j!=None:
            if i.val<j.val:
                res.val=i.val
                i=i.next
            else:
                res.val=j.val
                j=j.next
            res.next=ListNode(0)
            prev=res
            res=res.next
            continue
        if i!=None and j==None:
            res.val=i.val
            i=i.next
            res.next=ListNode(0)
            prev=res
            res=res.next
            continue
        if j!=None and i==None:
            res.val=j.val
            j=j.next
            res.next=ListNode(0)
            prev=res
            res=res.next
            continue
    prev.next=None
    return myres



def mergeKLists(lists):
    if len(lists)==0:
        return None
    k=len(lists)
    if k==1:
        return lists[0]
    while k!=1:
        tempL=[]
        if k%2==1:
            for i in range(int(k/2)):
                curr=merge2Lists(lists[i*2],lists[i*2+1])
                tempL.append(curr)
            tempL.append(lists[k-1])
            lists=tempL
            k=len(lists)
            continue
        if k%2==0:
            for i in range(int(k/2)):
                curr=merge2Lists(lists[i*2],lists[i*2+1])
                tempL.append(curr)
            lists=tempL
            k=len(lists)
            continue
    
    return lists[0]






i=ListNode(1)
i.next=ListNode(4)
i.next.next=ListNode(5)

j=ListNode(1)
j.next=ListNode(3)
j.next.next=ListNode(4)

k=ListNode(2)
k.next=ListNode(6)

res=merge2Lists(i,j)

printList(res)

lists=[i,j,k]

newRes=mergeKLists(lists)

printList(newRes)
