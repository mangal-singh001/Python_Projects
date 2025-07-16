
import time 
import threading
from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
        
    def enqueue(self,val):
        self.container.appendleft(val)
        
    def dequeue(self):
        if len(self.container) == 0:
            print("Queue is empty")
            return
        
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
food = Queue()

def place_order(orders):
    for order in orders:
        print(f"Placing order for : {order}")
        food.enqueue(order)
        time.sleep(0.5)
        
def serve_order():
    time.sleep(1)
    while True:
        d = food.dequeue()
        
        print(f"Now serving : {d}")
        time.sleep(2)
        
        if d == None:
            break
        
if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_order,args=[orders,])
    t2 = threading.Thread(target=serve_order)
    
    t1.start()
    t2.start()





