### LRU cache using Arrays: (utter flop project). Best example to tell the difference between arrays and Linked lists (benefits of using LL vs arrays) ###

# ptr=0
# totalCap = 0
# myQueue = 0
# myDict = 0
# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         global ptr
#         global totalCap
#         global myQueue
#         global myDict
#         totalCap = capacity
#         myQueue = [0]*capacity
#         ptr=0
#         myDict = {}
#         #myIndexDict = {}
        

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         #print "get "+str(key)
#         #print myQueue
#         global ptr
#         global totalCap
#         global myQueue
#         global myDict
#         if key not in myDict.keys():
#             #print "ret : "+str(-1)
#             return -1
#             #myIndexDict[key]=ptr
#         if myQueue.index(key)==ptr-1:
#             #print "ret : "+str(myDict[key])
#             return myDict[key]
#         if ptr==totalCap:
#             if myQueue.index(key)==0:
#                 #print "hi"
#                 myQueue=myQueue[1:]+[key]
#                 #print "ret : "+str(myDict[key])
#                 #print "myQueue: "+str(myQueue)
#                 return myDict[key]
#             else:
#                 #print "hello"
#                 #print "temp: "+str(myQueue)
#                 temp=myQueue.index(key)
#                 #print "temp2: "+str(myQueue[0:temp-1])
#                 myQueue=myQueue[0:temp]+myQueue[temp+1:]+[key]
#                 #print "ret : "+str(myDict[key])
#                 #print "myQueue: "+str(myQueue)
#                 return myDict[key]
#         else:
#             if myQueue.index(key)==0:
#                 myQueue=myQueue[1:ptr]+[key]+myQueue[ptr:]
#                 #print "ret : "+str(myDict[key])
#                 #print "myQueue: "+str(myQueue)
#                 return myDict[key]
#             else:
#                 temp=myQueue.index(key)
#                 myQueue=myQueue[0:temp]+myQueue[temp+1:ptr]+[key]+myQueue[ptr:]
#                 #print "ret : "+str(myDict[key])
#                 #print "myQueue: "+str(myQueue)
#                 return myDict[key]
            

        

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         global ptr
#         global totalCap
#         global myQueue
#         global myDict
#         #print "put "+str(key)+" : "+str(value)
#         if key in myDict.keys():
#             myDict[key]=value
#             if ptr==(totalCap):
#                 if myQueue.index(key)==0:
#                     #print "before cpy: "+str(myQueue)
#                     myQueue=myQueue[1:]+[key]
#                     #print "put "+str(key)+" : "+str(value)
#                     #print "myQueue: "+str(myQueue)
#                 elif(myQueue.index(key)<(len(myQueue)-1)):
#                     temp=myQueue.index(key)
#                     myQueue=myQueue[0:temp]+myQueue[temp+1:]+[key]
#                     #print "myQueue: "+str(myQueue)
#             else:
#                 if myQueue.index(key)==0:
#                     myQueue=myQueue[1:ptr]+[key]+myQueue[ptr:]
#                     #print "myQueue: "+str(myQueue)
#                 else:
#                     temp=myQueue.index(key)
#                     myQueue=myQueue[0:temp]+myQueue[temp+1:ptr]+[key]+myQueue[ptr:]
#                     #print "myQueue: "+str(myQueue)
#             return    
#         if ptr<(totalCap):
#             myQueue[ptr]=key
#             #myIndexDict[key]=ptr
#             ptr = ptr+1
#             myDict[key]=value
#             #print "myQueue: "+str(myQueue)
#         else:
#             #print myQueue
#             del myDict[myQueue[0]]
#             myQueue=myQueue[1:]+[0]
#             myQueue[ptr-1]=key
#             #myIndexDict[key]=ptr
#             myDict[key]=value
#             #print "myQueue: "+str(myQueue)
#         return
            
##### LL trials:

class node():
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.ct=0
        self.cap=capacity
        self.head=node(0,0)
        self.tail=node(0,0)
        self.myDict = dict()
        self.head.next=self.tail
        self.tail.prev=self.head
    def _add(self,key,val):
        newNode=node(key,val)
        newNode.prev=self.head
        newNode.next=self.head.next
        self.head.next.prev=newNode
        self.head.next=newNode
        self.myDict[key]=newNode
        #self.ct=self.ct+1
    
    def _remove(self,key):
        myNode = self.myDict[key]
        myNode.next.prev=myNode.prev
        myNode.prev.next=myNode.next
        del self.myDict[key]
        #self.ct=self.ct-1
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #print self.myDict
        try:
            myNode = self.myDict[key]
            tempVal=self.myDict[key].val
            self._remove(key)
            self._add(key,tempVal)
            return tempVal
        except:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #print self.myDict
        try:
            myNode=self.myDict[key]
            self._remove(key)
            self._add(key,value)
        except:
            if self.ct<self.cap:
                self._add(key,value)
                self.ct=self.ct+1
            else:
                tempKey = self.tail.prev.key
                self._remove(tempKey)
                self._add(key,value)                
    

#myCache = LRUCache(3)
myCache = LRUCache(2)
myCache.put(2,1)
myCache.put(1,1)
print(myCache.get(2))
myCache.put(3,5)
print(myCache.get(1))
print(myCache.get(3))
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)