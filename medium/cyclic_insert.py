"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head==None:
            newNode=Node(insertVal)
            head=newNode
            head.next=head
            return head
        elif head.next==head:
            newNode=Node(insertVal)
            head.next=newNode
            newNode.next=head
            return head
        else:
            ret=head
            curr=head
            prev=curr
            tempHead=head
            
            #print tempHead.val
            
            curr=curr.next
            while curr!=tempHead:
                if prev.val>curr.val:
                    break
                prev=curr
                curr=curr.next
            tempHead=curr
            
            #print tempHead.val
            
            #prev=tempHead
            curr=tempHead
            
            #curr=curr.next
            if prev.val<=insertVal<=curr.val:
                newNode=Node(insertVal)
                prev.next=newNode
                newNode.next=curr
                #print "hi"
                return ret
            prev=curr
            curr=curr.next
            
            while curr!=tempHead:
                if prev.val<=insertVal<=curr.val:
                    newNode=Node(insertVal)
                    prev.next=newNode
                    newNode.next=curr
                    #print "yo"
                    return ret
                prev=curr
                curr=curr.next
            
            if insertVal>=prev.val:
                newNode=Node(insertVal)
                prev.next=newNode
                newNode.next=curr
                return ret
            if insertVal<=curr.val:
                newNode=Node(insertVal)
                prev.next=newNode
                newNode.next=curr
                #print "ho"
                return ret
                    