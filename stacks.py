class Stack:
    def __init__(self):
        self.stack = []
    
    #add a value to the stack
    def push(self, item):
        return self.stack.append(item)

    #deletes a value from the top of the stack
    def pop(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack.pop()

    #display the stack
    def display(self):
        print(self.stack)



x = Stack()

print("initial stack")
for i in range(10):
    x.push(i)
x.display()

x.pop()

print("After it has been pop")
x.display() 