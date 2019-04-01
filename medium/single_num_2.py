
#using set  (memory extra. not desirable)
def single_num(nums):
        mySet=set(nums)
        mySum=sum(mySet)
        
        return (3*mySum-sum(nums))/2

#bit manipulation - didn't get
#def single_num(nums):

            

nums=[9,9,6,9]
print (single_num(nums))