# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#class Solution(object):
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1==None and l2==None:
        return None
    if l1==None:
        return l2
    if l2==None:
        return l1
    res=ListNode(None)
    temp=res
    while l1!=None or l2!=None:
        temp.next=ListNode(None)
        temp=temp.next
        if l1!=None and l2!=None:
            if l1.val>l2.val:
                temp.val=l2.val
                l2=l2.next
            elif l1.val<l2.val:
                temp.val=l1.val
                l1=l1.next
            else:
                temp.val=l1.val
                l1=l1.next
                temp.next=ListNode(None)
                temp=temp.next
                temp.val=l2.val
                l2=l2.next
            continue

        if l1!=None:
            temp.val=l1.val
            l1=l1.next
            continue

        if l2!=None:
            temp.val=l2.val
            l2=l2.next
            continue
    
    return res.next

N1=ListNode(1)
N2=N1.next=ListNode(2)
N3=N2.next=ListNode(4)

N4=ListNode(1)
N2=N4.next=ListNode(3)
N3=N2.next=ListNode(4)

a=mergeTwoLists(N1,N4)

while a!=None:
    print (a.val)
    a=a.next

