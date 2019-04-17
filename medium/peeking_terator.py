# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """

        self.iterator=iterator
        self.flag=0
        self.curr=None
        if self.iterator.hasNext():
            self.peeker=self.iterator.next()
        else:
            self.peeker=None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

        if self.flag==0:
            return self.peeker
        else:
            return None
        

    def next(self):
        """
        :rtype: int
        """

        if self.iterator.hasNext():
            self.curr=self.peeker
            self.peeker=self.iterator.next()
            return self.curr
        else:
            self.flag=1
            return self.peeker
        
        
        

    def hasNext(self):
        """
        :rtype: bool
        """

        if self.flag==0:
            return True
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].