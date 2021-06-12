class Stack:
    def __init__(self):
        self.stack = []
    
    #add a value to the to the queuew
    def enqueue(self, item):
        return self.stack.append(item)

    #deletes a value from the front of the queue
    def dequeue(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack.pop(0)

    #display the stack
    def display(self):
        print(self.stack)



x = Stack()

print("initial stack")
for i in range(10):
    x.enqueue(i)
x.display()

x.dequeue()

print("After it has been pop")
x.display() 