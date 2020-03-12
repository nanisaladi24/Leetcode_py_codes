from threading import Event
import threading
import os

def printFizz():
    print ("\nFizz\n")
    return

def printBuzz():
    print ("\nBuzz\n")
    return

def printFizzBuzz():
    print ("\nFizzBuzz\n")
    return

def printNumber(k):
    print ("\n"+str(k)+"\n")
    return


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.event1 = Event()
        self.event2 = Event()
        self.event3 = Event()
        self.event4 = Event()
        self.curr=1
        self.event1.set()
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """

        while self.curr<=self.n:
            #print("hello")
            #print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
            #print("ID of process running task 1: {}".format(os.getpid())) 
            self.event2.wait()
            self.event2.clear()
            if self.curr>self.n:
                break
            #print ("yo")
            if self.curr%3==0 and self.curr%15!=0:
                printFizz()
                self.curr=self.curr+1
                self.event1.set()
        
        return
        
    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """


        while self.curr<=self.n:
            #print ("hi")
            #print("Task 2 assigned to thread: {}".format(threading.current_thread().name)) 
            #print("ID of process running task 2: {}".format(os.getpid())) 
            self.event3.wait()
            self.event3.clear()
            if self.curr>self.n:
                break
            #print ("ya")
            if self.curr%5==0 and self.curr%15!=0:
                printBuzz()
                self.curr=self.curr+1
                self.event1.set()
        
        return
        
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """


        while self.curr<=self.n:
            #print ("bye")
            #print("Task 3 assigned to thread: {}".format(threading.current_thread().name)) 
            #print("ID of process running task 3: {}".format(os.getpid())) 
            self.event4.wait()
            self.event4.clear()
            if self.curr>self.n:
                break
            #print ("bo")
            if self.curr%15==0:
                printFizzBuzz()
                self.curr=self.curr+1
                self.event1.set()
        
        return

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """


        while self.curr<=self.n:
            #print ("hibye")
            #print("Task 4 assigned to thread: {}".format(threading.current_thread().name)) 
            #print("ID of process running task 4: {}".format(os.getpid())) 
            if self.curr>1:
                self.event1.wait()
            #print("wo")
            if self.curr>self.n:
                self.event2.set()
                self.event3.set()
                self.event4.set()
                #print ("reached")
                break
            #print(self.curr)
            if self.curr%3==0 or self.curr%5==0:
                self.event1.clear()
                self.event2.set()
                self.event3.set()
                self.event4.set()
            else:
                printNumber(self.curr)
                self.curr=self.curr+1
            
            
        self.event2.set()
        self.event3.set()
        self.event4.set()
        
        return

if __name__ == "__main__": 
    # print ID of current process 
    #print("ID of process running main program: {}".format(os.getpid())) 

    # print name of main thread 
    #print("Main thread name: {}".format(threading.current_thread().name)) 

    myFB = FizzBuzz(150)

    # creating threads 
    t1 = threading.Thread(target=myFB.fizz,args=({printFizz:()}), name='t1') 
    t2 = threading.Thread(target=myFB.buzz,args=({printBuzz:()}), name='t2')  
    t3 = threading.Thread(target=myFB.fizzbuzz,args=({printFizzBuzz:()}), name='t3') 
    t4 = threading.Thread(target=myFB.number,args=({printNumber:()}), name='t4')  

    # starting threads 
    t1.start() 
    t2.start() 
    t3.start()
    t4.start()

    # wait until all threads finish 
    t1.join() 
    t2.join()
    t3.join()
    t4.join() 