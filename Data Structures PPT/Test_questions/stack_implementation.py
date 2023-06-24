"""
Implement a stack using a list in Python. Include the necessary methods such as push, pop, and isEmpty.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,x) -> None:
        self.stack.append(x)
        return
    
    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        return val 

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack

st = Stack()

# checking stack is empty or not
print(f"is Empty = {st.isEmpty()}")
# trying to get top element
print(f"Top element = {st.peek()}")
# trying to pop on empty stack
print(f"Popped element = {st.pop()}")

# inserting elements
for i in range(1,10):
    st.push(i)

# printing top element
print(f"Top element = {st.peek()}")
# popping the element
print(f"Popped element = {st.pop()}")
# printing top element
print(f"Top element = {st.peek()}")
# checking stack is empty or not
print(f"is Empty = {st.isEmpty()}")
