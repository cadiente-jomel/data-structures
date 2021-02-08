# queue using list
# btc_stock_price_queue = []
# btc_stock_price_queue.insert(0, 4000)
# btc_stock_price_queue.insert(0, 1000)
# btc_stock_price_queue.insert(0, 3000)

# print(btc_stock_price_queue)
# btc_stock_price_queue.pop()
# btc_stock_price_queue.pop()
# btc_stock_price_queue.pop()
# print(btc_stock_price_queue)

# using deque instead
from collections import deque

# q = deque()

# q.appendleft('btc')
# q.appendleft('etc')
# q.appendleft('ltc')

# print(q)
# q.pop()
# print(q)


# class implementation

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        return self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0
        
    def size(self):
        return len(self.buffer)

q = Queue()

q.enqueue('btc')
q.enqueue('etc')
q.enqueue('ltc')
print(q.buffer)
q.dequeue()
q.dequeue()
q.dequeue()
print(q.is_empty())
print(q.buffer)