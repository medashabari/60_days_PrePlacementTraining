"""
Implement a queue using a list in Python. Include the necessary methods such as enqueue, dequeue, and isEmpty.
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,x):
        self.queue.append(x)
        return 

    def dequeue(self):
        if not self.queue:
            return None
        val = self.queue.pop(0)
        return val

    def isEmpty(self)-> bool :
        return not self.queue


q = Queue()

# checking queue is empty or not
print(f"is Empty = {q.isEmpty()}")

# trying to dequeu an element on empty queue
print(f"Popped element = {q.dequeue()}")

# inserting elements
for i in range(1,10):
    q.enqueue(i)


# dequeueing the element
print(f"dequeued element = {q.dequeue()}")
# checking queue is empty or not
print(f"is Empty = {q.isEmpty()}")