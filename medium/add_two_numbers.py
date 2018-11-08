class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None

def addTwoNumbers(l1,l2):
    #print l1.val
    l3=ListNode(0)
    pl1=l1
    pl2=l2
    pl3=l3
    #print pl3.val
    while pl1!=None and pl2!=None:
        pl3.next=ListNode((pl3.val+pl1.val+pl2.val)/10)
        pl3.val=(pl3.val+pl1.val+pl2.val)%10
        pl1=pl1.next
        pl2=pl2.next
        pl3=pl3.next
    if pl1==None and pl2!=None:
        while pl2!=None:
            pl3.next=ListNode((pl3.val+pl2.val)/10)
            pl3.val=(pl3.val+pl2.val)%10
            pl2=pl2.next
            pl3=pl3.next
    if pl2==None and pl1!=None:
        while pl1!=None:
            pl3.next=ListNode((pl3.val+pl1.val)/10)
            pl3.val=(pl3.val+pl1.val)%10
            pl1=pl1.next
            pl3=pl3.next
    prevl3=l3
    currl3=l3.next
    while currl3.next!=None:
        prevl3=currl3
        currl3=currl3.next
    if currl3.val==0:
        prevl3.next=None
    return l3
        
l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)
print str(l1.val)+" -> "+str(l1.next.val)+" -> "+str(l1.next.next.val)
print str(l2.val)+" -> "+str(l2.next.val)+" -> "+str(l2.next.next.val)
l3=addTwoNumbers(l1, l2)

print str(l3.val)+" -> "+str(l3.next.val)+" -> "+str(l3.next.next.val)